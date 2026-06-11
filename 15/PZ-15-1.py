import sqlite3 as sq
from data import INITIAL_DATA

DB_NAME = 'parik.db'


def init_db():
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Услуги (
            id INTEGER PRIMARY KEY,
            master TEXT NOT NULL,
            client TEXT NOT NULL,
            pol INTEGER NOT NULL DEFAULT 1,
            strizhka TEXT NOT NULL,
            stoimost REAL NOT NULL
        )""")
        
        cur.execute("SELECT COUNT(*) FROM Услуги")
        if cur.fetchone()[0] == 0:
            cur.executemany(
                "INSERT INTO Услуги (id, master, client, pol, strizhka, stoimost) VALUES (?, ?, ?, ?, ?, ?)",
                INITIAL_DATA
            )


def show_table(title="Все записи"):
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Услуги ORDER BY id")
        rows = cur.fetchall()
    
    print(f"\n--- {title} ---")
    print(f"{'ID':<4} {'Мастер':<15} {'Клиент':<15} {'Пол':<6} {'Стрижка':<20} {'Цена':<8}")
    print("-" * 70)
    for row in rows:
        pol_str = "Жен" if row[3] == 2 else "Муж"
        print(f"{row[0]:<4} {row[1]:<15} {row[2]:<15} {pol_str:<6} {row[4]:<20} {row[5]:<8.2f}")
    print("-" * 70)


def add_record():
    print("\n--- Добавление записи ---")
    try:
        rec_id = int(input("ID записи: ").strip())
        master = input("ФИО мастера: ").strip()
        client = input("ФИО клиента: ").strip()
        pol = int(input("Пол (1-Муж, 2-Жен): ").strip())
        strizhka = input("Название стрижки: ").strip()
        stoimost = float(input("Стоимость: ").strip())
        
        if not (master and client and strizhka):
            raise ValueError("Поля не могут быть пустыми")
            
        with sq.connect(DB_NAME) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO Услуги (id, master, client, pol, strizhka, stoimost) VALUES (?, ?, ?, ?, ?, ?)",
                (rec_id, master, client, pol, strizhka, stoimost)
            )
        print("Запись успешно добавлена!")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")


def search_records():
    print("\n--- Поиск записей ---")
    print("1. По ID записи")
    print("2. По фамилии клиента/мастера (LIKE)")
    print("3. По диапазону стоимости (BETWEEN)")
    
    choice = input("Выберите вариант поиска (1-3): ").strip()
    
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        rows = []
        
        try:
            if choice == '1':
                rec_id = int(input("Введите ID: ").strip())
                cur.execute("SELECT * FROM Услуги WHERE id = ?", (rec_id,))
                rows = cur.fetchall()
                
            elif choice == '2':
                query = input("Введите часть имени: ").strip()
                cur.execute(
                    "SELECT * FROM Услуги WHERE client LIKE ? OR master LIKE ?",
                    (f"%{query}%", f"%{query}%")
                )
                rows = cur.fetchall()
                
            elif choice == '3':
                min_price = float(input("Минимальная цена: ").strip())
                max_price = float(input("Максимальная цена: ").strip())
                cur.execute(
                    "SELECT * FROM Услуги WHERE stoimost BETWEEN ? AND ? ORDER BY stoimost",
                    (min_price, max_price)
                )
                rows = cur.fetchall()
            else:
                print("Неверный выбор!")
                return
                
        except ValueError:
            print("Ошибка: введите корректные числовые значения.")
            return

    if rows:
        show_table("Результаты поиска")
    else:
        print("Ничего не найдено.")


def update_record():
    print("\n--- Редактирование записи ---")
    print("1. Изменить стоимость по ID")
    print("2. Изменить ФИО мастера для конкретного клиента")
    print("3. Изменить название стрижки для всех записей мастера")
    
    choice = input("Выберите вариант редактирования (1-3): ").strip()
    
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        try:
            if choice == '1':
                rec_id = int(input("ID записи: ").strip())
                new_price = float(input("Новая стоимость: ").strip())
                cur.execute("UPDATE Услуги SET stoimost = ? WHERE id = ?", (new_price, rec_id))
                
            elif choice == '2':
                client_name = input("ФИО клиента: ").strip()
                new_master = input("Новое ФИО мастера: ").strip()
                cur.execute("UPDATE Услуги SET master = ? WHERE client = ?", (new_master, client_name))
                
            elif choice == '3':
                old_master = input("ФИО мастера (кого меняем): ").strip()
                new_haircut = input("Новое название стрижки: ").strip()
                cur.execute("UPDATE Услуги SET strizhka = ? WHERE master = ?", (new_haircut, old_master))
            else:
                print("Неверный выбор!")
                return
                
            if cur.rowcount > 0:
                print("Данные обновлены!")
            else:
                print("Записи для обновления не найдены.")
                
        except ValueError:
            print("Ошибка ввода данных.")


def delete_record():
    print("\n--- Удаление записи ---")
    print("1. Удалить по ID")
    print("2. Удалить все записи клиента")
    print("3. Удалить дешевые услуги (ниже указанной цены)")
    
    choice = input("Выберите вариант удаления (1-3): ").strip()
    
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        try:
            if choice == '1':
                rec_id = int(input("ID записи: ").strip())
                cur.execute("DELETE FROM Услуги WHERE id = ?", (rec_id,))
                
            elif choice == '2':
                client_name = input("ФИО клиента для удаления: ").strip()
                cur.execute("DELETE FROM Услуги WHERE client = ?", (client_name,))
                
            elif choice == '3':
                max_price = float(input("Удалить все услуги дешевле этой суммы: ").strip())
                cur.execute("DELETE FROM Услуги WHERE stoimost < ?", (max_price,))
            else:
                print("Неверный выбор!")
                return
                
            if cur.rowcount > 0:
                print(f"Удалено записей: {cur.rowcount}")
            else:
                print("Ничего не удалено.")
                
        except ValueError:
            print("Ошибка ввода данных.")


def main():
    init_db()
    
    while True:
        print("\n=== ПАРИКМАХЕРСКАЯ ===")
        print("1. Показать все записи")
        print("2. Добавить запись")
        print("3. Поиск (3 запроса)")
        print("4. Редактирование (3 запроса)")
        print("5. Удаление (3 запроса)")
        print("0. Выход")
        
        choice = input("\nВыберите действие: ").strip()
        
        if choice == '1':
            show_table()
        elif choice == '2':
            add_record()
        elif choice == '3':
            search_records()
        elif choice == '4':
            update_record()
        elif choice == '5':
            delete_record()
        elif choice == '0':
            print("Работа завершена.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()