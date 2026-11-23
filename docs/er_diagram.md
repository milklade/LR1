

\# ER-модель предметной области



\## Тема

Курсы повышения квалификации.



\## Описание

База данных предназначена для хранения информации о преподавателях, учебных группах, предметах и распределении учебной нагрузки.



\## ER-диаграмма



```mermaid

erDiagram

&#x20;   Teacher ||--o{ TeachingLoad : conducts

&#x20;   StudentGroup ||--o{ TeachingLoad : receives

&#x20;   Subject ||--o{ TeachingLoad : includes



&#x20;   Teacher {

&#x20;       int teacher\_id PK

&#x20;       string surname

&#x20;       string first\_name

&#x20;       string patronymic

&#x20;       string phone

&#x20;       int work\_experience

&#x20;   }



&#x20;   StudentGroup {

&#x20;       int group\_id PK

&#x20;       string group\_name

&#x20;       string specialty

&#x20;       string department

&#x20;       int student\_count

&#x20;   }



&#x20;   Subject {

&#x20;       int subject\_id PK

&#x20;       string subject\_name

&#x20;   }



&#x20;   TeachingLoad {

&#x20;       int load\_id PK

&#x20;       int teacher\_id FK

&#x20;       int group\_id FK

&#x20;       int subject\_id FK

&#x20;       string lesson\_type

&#x20;       int hours

&#x20;       decimal hourly\_rate

&#x20;   }

```



\## Описание таблиц



\### 1. Teacher — преподаватели

Хранит анкетные данные преподавателей и стаж работы.



Первичный ключ: teacher\_id.



\### 2. StudentGroup — учебные группы

Хранит название группы, специальность, отделение и количество студентов.



Первичный ключ: group\_id.



\### 3. Subject — предметы

Хранит названия учебных предметов.



Первичный ключ: subject\_id.



\### 4. TeachingLoad — учебная нагрузка

Хранит сведения о распределении занятий: преподавателе, группе, предмете, типе занятия, количестве часов и оплате за час.



Первичный ключ: load\_id.



Внешние ключи:

\- teacher\_id → Teacher.teacher\_id

\- group\_id → StudentGroup.group\_id

\- subject\_id → Subject.subject\_id



\## Связи между таблицами



\- Teacher и TeachingLoad — один ко многим.

\- StudentGroup и TeachingLoad — один ко многим.

\- Subject и TeachingLoad — один ко многим.



Таблица TeachingLoad связывает преподавателей, учебные группы и предметы.



\## Обоснование выбора основной сущности



Для дальнейших лабораторных работ выбрана сущность Teacher.



Она является самостоятельной сущностью и содержит шесть полей. StudentGroup содержит пять полей, Subject — два поля.



TeachingLoad является зависимой ассоциативной сущностью, поэтому не рассматривается как кандидат на главную самостоятельную сущность.



