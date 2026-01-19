import json
import os
from collections import defaultdict

def analyze_swagger(file_path):
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    info = data.get('info', {})
    base_path = data.get('basePath', '')
    paths = data.get('paths', {})
    definitions = data.get('definitions', {})
    
    report = {
        "title": info.get('title', 'Unknown API'),
        "version": info.get('version', 'Unknown'),
        "description": info.get('description', ''),
        "base_path": base_path,
        "tags": defaultdict(list),
        "models": {}
    }
    
    # Analyze Paths
    for path, methods in paths.items():
        for method, details in methods.items():
            tags = details.get('tags', ['Other'])
            for tag in tags:
                report["tags"][tag].append({
                    "path": path,
                    "method": method.upper(),
                    "summary": details.get('summary', ''),
                    "operationId": details.get('operationId', '')
                })
                
    # Analyze Definitions (Models)
    for model_name, model_details in definitions.items():
        properties = model_details.get('properties', {})
        props_summary = []
        for prop_name, prop_details in properties.items():
            prop_type = prop_details.get('type', 'object')
            if '$ref' in prop_details:
                prop_type = f"Ref({prop_details['$ref'].split('/')[-1]})"
            elif prop_type == 'array':
                items = prop_details.get('items', {})
                if '$ref' in items:
                    prop_type = f"Array[Ref({items['$ref'].split('/')[-1]})]"
                else:
                    prop_type = f"Array[{items.get('type', 'object')}]"
            
            props_summary.append({
                "name": prop_name,
                "type": prop_type,
                "description": prop_details.get('description', '')
            })
        report["models"][model_name] = props_summary
        
    return report

def generate_markdown_report(public_report, client_report, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Go-CRM API Structure Analytics Report\n\n")
        f.write("Этот отчет сгенерирован автоматически для анализа возможностей API Go-CRM.\n\n")
        
        for report in [public_report, client_report]:
            if not report:
                continue
            
            f.write(f"## {report['title']} (v{report['version']})\n")
            f.write(f"**Base Path:** `{report['base_path']}`\n\n")
            f.write(f"{report['description']}\n\n")
            
            f.write("### Сущности и Методы (Endpoints)\n")
            for tag, endpoints in sorted(report["tags"].items()):
                f.write(f"#### Tag: {tag}\n")
                f.write("| Path | Method | Summary |\n")
                f.write("| :--- | :--- | :--- |\n")
                for ep in endpoints:
                    f.write(f"| `{ep['path']}` | **{ep['method']}** | {ep['summary']} |\n")
                f.write("\n")
            
            f.write("### Модели Данных (Schemas)\n")
            for model_name, props in sorted(report["models"].items()):
                f.write(f"#### {model_name}\n")
                f.write("| Property | Type | Description |\n")
                f.write("| :--- | :--- | :--- |\n")
                for p in props:
                    f.write(f"| {p['name']} | `{p['type']}` | {p['description']} |\n")
                f.write("\n---\n\n")

if __name__ == "__main__":
    public_file = "Public API.json"
    client_file = "Client API.json"
    output_report = "API_REPORT.md"
    
    print(f"Analysing {public_file}...")
    pub_rep = analyze_swagger(public_file)
    
    print(f"Analysing {client_file}...")
    cli_rep = analyze_swagger(client_file)
    
    print(f"Generating report {output_report}...")
    generate_markdown_report(pub_rep, cli_rep, output_report)
    print("Done!")
