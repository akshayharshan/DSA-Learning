# 📁 Flutter Project File Structure

This project follows a **feature-based, scalable architecture** designed for maintainability and team collaboration.

---

## 🧱 Root Structure

```
lib/
├── core/
├── features/
├── main.dart
```

---

## 🧩 Core Layer (Shared Across App)

```
core/
├── constants/        # App-wide constants (colors, strings, etc.)
├── theme/            # Theme configuration (ThemeData)
├── layout/           # Responsive helpers
├── widgets/          # Reusable UI components
└── utils/            # Utility/helper functions
```

### Purpose:

* Avoid duplication
* Centralize shared logic and styling

---

## 🚀 Features Layer (Feature-Based Modules)

```
features/
├── auth/
├── home/
├── profile/
```

Each feature contains:

```
feature_name/
├── data/             # API, models, repository implementations
├── domain/           # Business logic (entities, use cases)
└── presentation/     # UI (screens, widgets, state)
```

---

## 🖥️ Presentation Layer

```
presentation/
├── screens/          # Full pages
├── widgets/          # Feature-specific widgets
└── state/            # Bloc / Riverpod / Controllers
```

---

## 🌐 Data Layer

```
data/
├── models/           # JSON models
├── repositories/     # Implementation
└── datasources/      # API / DB calls
```

---

## 🧠 Domain Layer

```
domain/
├── entities/         # Core business objects
├── repositories/     # Abstract contracts
└── usecases/         # Business logic
```

---

## 🎯 Key Principles

* Feature-based separation
* UI separated from logic
* Scalable for large teams
* Easy to refactor and extend

---

## 🚫 Avoid

* Global “screens/” or “widgets/” folders without features
* Mixing API calls inside UI
* Large monolithic files

---

## ✅ Summary

This structure ensures:

* Clean separation of concerns
* Easy onboarding for new developers
* Maintainable and scalable codebase
