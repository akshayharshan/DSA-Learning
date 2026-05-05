# 🧑‍💻 Flutter Coding Standards

This document defines coding practices to ensure consistency, readability, and maintainability.

---

## 🧱 General Principles

* Keep code **simple and readable**
* Prefer **composition over complexity**
* Follow **single responsibility principle**

---

## 📦 File Naming

Use snake_case:

```
user_model.dart
auth_repository.dart
login_screen.dart
```

---

## 🧩 Class Naming

Use PascalCase:

```
class LoginScreen {}
class AuthRepository {}
```

---

## 🔹 Widget Guidelines

### ✅ Keep Widgets Small

Bad:

```
One widget with 500+ lines
```

Good:

```
LoginForm
LoginButton
HeaderSection
```

---

### ✅ Stateless vs Stateful

* Use `StatelessWidget` whenever possible
* Use `StatefulWidget` only when necessary

---

## ⚙️ Business Logic Separation

### ❌ Avoid

```
onPressed: () async {
  await api.login();
}
```

### ✅ Use

```
onPressed: () => bloc.login()
```

---

## 🎨 Styling Rules

### ❌ Avoid

```
TextStyle(fontSize: 18)
```

### ✅ Use centralized styles

```
AppTextStyles.heading
```

---

## 📐 Layout Rules

* Avoid fixed sizes
* Use:

  * Expanded
  * Flexible
  * MediaQuery (when needed)

---

## 🔁 Reusability

* Extract reusable components into:

```
core/widgets/
```

---

## 🧪 Null Safety

* Always handle null safely
* Avoid forced `!` unless absolutely sure

---

## 🧼 Code Cleanliness

* Remove unused imports
* Keep functions short
* Use meaningful variable names

---

## 🔄 State Management

Use structured state management:

* Bloc OR Riverpod (recommended)

---

## ✅ Summary

Following these standards ensures:

* Consistent codebase
* Easier debugging
* Better team collaboration
