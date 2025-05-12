Цей проєкт реалізує просту систему для побудови ланцюга блоків за голосами користувачів, з подальшим перетворенням у бінарне дерево. Потім визначається тип дерева (повне/досконале) та виводяться обходи.

## Структура проєкту

- `lab4.py` — головний файл, який:
  - приймає список блоків з параметрами `id`, `view`, `value`
  - приймає голоси за блоки
  - будує ланцюг блоків за зростанням `view` тільки для проголосованих
  - створює з цього ланцюга бінарне дерево
  - визначає тип дерева (повне/досконале)
  - виконує обходи: pre-order, in-order, post-order

## Схема виконання 

```mermaid
flowchart TD
    Start([Початок])
    InputBlocks["Введення блоків\n(ID, View, Value)"]
    InputVotes["Введення голосів"]
    BuildChain["Побудова ланцюга\nна основі View і голосів"]
    BuildTree["Формування бінарного дерева"]
    DetermineType["Визначення типу дерева"]
    Traversals["Обходи: Pre/In/Post-order"]
    End([🏁 Кінець])

    Start --> InputBlocks
    InputBlocks --> InputVotes
    InputVotes --> BuildChain
    BuildChain --> BuildTree
    BuildTree --> DetermineType
    DetermineType --> Traversals
    Traversals --> End
