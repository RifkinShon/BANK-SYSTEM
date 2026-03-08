raise ValueError("ערך לא תקין")        # ערך שגוי
raise TypeError("סוג לא תקין")         # סוג שגוי (int במקום str)
raise KeyError("מפתח לא קיים")         # מפתח לא קיים במילון
raise IndexError("אינדקס לא קיים")     # אינדקס לא קיים ברשימה
raise AttributeError("תכונה לא קיימת") # תכונה לא קיימת באובייקט
raise FileNotFoundError("קובץ לא נמצא") # קובץ לא נמצא
raise ZeroDivisionError("חלוקה באפס")  # חלוקה באפס
raise PermissionError("אין הרשאה")     # אין הרשאה
raise TimeoutError("פג תוקף")          # פג תוקף
raise NotImplementedError("לא ממומש")  # פונקציה שעוד לא ממומשת
raise RuntimeError("שגיאת ריצה") 