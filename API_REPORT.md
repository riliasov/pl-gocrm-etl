# Go-CRM API Structure Analytics Report

Этот отчет сгенерирован автоматически для анализа возможностей API Go-CRM.

## Go-CRM Public API (v3.0.2)
**Base Path:** `/api/v3`

Go-CRM `Public API` 
Представленные в этом разделе методы публичны и не требуют аутентификации.

### Сущности и Методы (Endpoints)
#### Tag: /centers
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/centers/{id}` | **GET** | Получение информации об конкретном центре |

#### Tag: /cities
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/cities` | **GET** | Получение информации об городах |
| `/cities/{id}` | **GET** | Получение информации об конкретном городе |
| `/cities/{id}/centers` | **GET** | Получение информации о центрах города |

#### Tag: /firms
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/firms` | **GET** | Получение списка Компаний из ЦРМ |
| `/firms/{id}` | **GET** | Получение информации об конкретной Компании |

#### Tag: /leads
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/leads` | **POST** | Добавление новой заявки в ЦРМ |

#### Tag: /users
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/users` | **GET** | Получение информации о сотрудниках |

### Модели Данных (Schemas)
#### ApiResponse
| Property | Type | Description |
| :--- | :--- | :--- |
| status | `string` | Статус выполнения операции на сервере |
| message | `string` | Сообщение, в случае возникновения ошибки. |
| validation_errors | `object` | Сообщение, в случае возникновения ошибок валидации. |
| data | `object` | Объекты передаваемых данных |

---

#### Center
| Property | Type | Description |
| :--- | :--- | :--- |
| id | `integer` | Уникадьный идентификатор центра |
| city | `string` | Наименование города в котором находится центр |
| cityAlias | `string` | Псевдоним города в котором находится центр |
| centerAlias | `string` | Псевдоним центра |
| address | `string` | Адрес центра |
| phone | `string` | Номер телефона центра |
| email | `string` | Электронный адрес центра |
| cityId | `integer` | Идентификатор города в котором находится центр |
| firmId | `integer` | Идентификатор Компании которой центр принадлежит |
| timezone | `string` | Временная зона для центра |
| description | `string` | Описание для центра |
| latitude | `string` | Широта |
| longitude | `string` | Долгота |
| siteStatus | `boolean` | Флаг для отображения на сайте |

---

#### City
| Property | Type | Description |
| :--- | :--- | :--- |
| id | `integer` | Уникадьный идентификатор города |
| alias | `string` | псевдоним города |
| name | `string` | Наименование города |
| site | `string` | ссылка на сайт |
| countryId | `integer` | Идентификатор страны |
| mobileAppWayId | `integer` | Идентификатор источника (для мобильного приложения) |

---

#### Firm
| Property | Type | Description |
| :--- | :--- | :--- |
| id | `integer` | Уникадьный идентификатор компании |
| nameFirm | `string` | Наименование компании |
| legalAddress | `string` | Юридический адрес |
| actualAddress | `string` | Фактический адрес |
| phone | `string` | Телефон |
| fax | `string` | Факс |
| email | `string` | Электронный адрес |
| ogrn | `string` | ОГРН |
| inn | `string` | ИНН |
| kpp | `string` | КПП |
| director | `string` | Директор |
| base | `string` | Основания для ведения деятельности |
| bank | `string` | Наименование банка |
| bik | `string` | БИК банка |
| rs | `string` | Расчётный счёт |
| ks | `string` | Кор.счёт |
| doc | `string` | ссылка на клиентский договор |
| welcomeMessage | `string` | Приветственное сообщение |
| createdAt | `string` | Дата добавления компании в систему в формате [ГГГГ-ММ-ДД чч:мм:сс] |

---

#### Lead
| Property | Type | Description |
| :--- | :--- | :--- |
| id | `integer` | Уникадьный идентификатор заявки |
| name | `string` | Имя Ребёнка |
| status | `string` | Статус заявки в системе |
| mail | `string` | Электронная почта |
| center_id | `integer` | Идентификатор центра посещения |
| phone | `string` | Номер телефона |
| fio | `string` | ФИО Родителя |
| birthday | `string` | Дата рождения (ГГГГ-ММ-ДД) |
| comment | `string` | Комментарий к заявке |
| way_id | `integer` |  |

---

#### User
| Property | Type | Description |
| :--- | :--- | :--- |
| id | `integer` | Уникадьный идентификатор пользователя |
| login | `string` | Логин сотрудника |
| name | `string` | Имя |
| displayName | `string` | Паблик имя сотрудника |
| isDisplay | `boolean` | Флаг для определения публичности. Если false, то в ЦРМ запретили отображать пользователя. |
| description | `string` | Бриф сотрудника |
| photo | `string` | ссылка на фото профиля |
| position | `integer` | Идентификатор должности, 2 - Директор, 3 - Администратор, 4 - Инструктор |
| centerId | `integer` | Идентификатор центра |
| center | `Ref(Center)` | Информация о центре, за которым закреплён сотрудник |

---

## Go-CRM Client API (v3.0.1)
**Base Path:** `/api/`

Go-CRM `Client  API` DOCS Description

### Сущности и Методы (Endpoints)
#### Tag: auth
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/auth/registration` | **POST** | Регистрация пользователя |
| `/auth/login` | **POST** | Авторизация пользователя |
| `/auth/logout` | **POST** | Выход |

#### Tag: client-hours
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/client-hours` | **GET** | Информация о занятиях клиента |
| `/client-hours/` | **POST** | Информация по записи клиента на занятие |

#### Tag: client-season-tickets
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/client-season-tickets` | **GET** | Информация по бонементам клиента |

#### Tag: clients
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/clients` | **GET** | Информация по клиентам |
| `/clients/(:num)` | **GET** | Обновление информация по клиенту |

#### Tag: debts
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/debts` | **GET** | Информация о задолженности |

#### Tag: hours
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/hours` | **GET** | Информация по расписанию |

#### Tag: payments
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/payments` | **GET** | Информация по эквайрингу |
| `/payments/` | **PUT** | Информация по проведению платежа |

#### Tag: profile
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/profile` | **GET** | Информация по профилю |
| `/profile/` | **PUT** | Обновление информация по профилю |

#### Tag: season-tickets
| Path | Method | Summary |
| :--- | :--- | :--- |
| `/season-tickets` | **GET** | Информация по абонементам |

### Модели Данных (Schemas)
