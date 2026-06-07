# Walphy
php and python app (for development only)


# PyWebKit Fusion: Hybrid Web + Desktop Application Framework

**Current Status:** Prototype / Development Alpha

## Project Credibility & Vision

This project represents a hybrid application architecture that bridges the gap between local desktop execution and dynamic web serving. The core concept is to run a lightweight Python web server (Flask) embedded within a PyQt5 WebEngineView, creating a desktop application whose UI is rendered via HTML/CSS/JS but retains full access to local system resources through the Python backend.

The architecture is inspired by tools like **Electron** but leverages Python's extensive ecosystem for data processing, system integration, and rapid backend development.

### Why This Matters

- **Unified Codebase:** Write your backend logic in Python and your frontend in standard web technologies.
- **Local-First Capability:** Perfect for internal tools, dashboards, data processing apps, or IoT controllers.
- **Extensibility:** Easily integrate PHP, Node.js, or any other local runtime alongside the Flask server.

## Project Structure

project-root/

    ├── appserver.py          # Flask backend server (API endpoints + static routes)
    ├── apis.py               # Modular route definitions (imported into appserver)
    ├── config.py             # Central configuration (paths, ports, directories)
    ├── myapp.py              # PyQt5 WebEngineView browser container (Main Application)
    ├── windows.py            # Alternate/legacy PyQt5 window implementation
    ├── runApp.bat            # Batch launcher (starts server + GUI)
    ├── whatsNext.txt         # Development roadmap / future feature list
    ├── templates/            # HTML/CSS/JS frontend files (served by Flask)
    ├── data/                 # Persistent local data storage
    ├── temp/                 # Temporary file storage
    └── servers/              # External runtimes (e.g., php-8.2.6)

## Current Features

| Feature | Status | Location |
|---------|--------|----------|
| Flask REST API server | ✅ Implemented | `appserver.py` |
| PyQt5 WebEngineView container | ✅ Implemented | `myapp.py` |
| Browser-style navigation (Back, Forward, Reload, Home) | ✅ Implemented | `myapp.py` |
| Dynamic URL bar with navigation | ✅ Implemented | `myapp.py` |
| Threaded server startup | ✅ Implemented | `myapp.py` |
| PHP server integration (via command line) | ✅ Prototype | `start_server()` in `myapp.py` |
| Sample CRUD API routes | ✅ Implemented | `appserver.py` |
| Centralized configuration | ✅ Implemented | `config.py` |

## Planned Enhancements (from `whatsNext.txt`)

| Feature | Description |
|---------|-------------|
| **devMode & usermode** | Separate development and production environments |
| **Node.js integration** | Live rendering / hot-reload for frontend frameworks |
| **Local & temporary databases** | SQLite, in-memory, or IndexedDB support |
| **DNS System & Security** | Local domain mapping, SSL, and request filtering |

## Getting Started

### Prerequisites

- Python 3.8+
- PyQt5 and PyQtWebEngine:
  ```bash
  pip install PyQt5 PyQtWebEngine Flask
  ```
- (Optional) PHP for legacy template serving – see `config["phpDir"]`

### Running the Application

1. **Configure paths** (if necessary) in `config.py`
2. **Launch the application** using the batch file:
   ```batch
   runApp.bat
   ```
   Or manually:
   ```bash
   python myapp.py
   ```

### What Happens at Runtime

1. `config.py` loads application settings (port: 999, directories, etc.)
2. `myapp.py` starts a Flask server in a background thread using `appserver.py`
3. PyQt5 launches a WebEngineView window pointing to `http://127.0.0.1:999`
4. The Flask server serves `templates/index.html` (if exists) or fallback routes
5. API endpoints are accessible via `http://127.0.0.1:999/api/resource`

### API Endpoints (Available)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns a simple HTML string |
| GET | `/api/resource` | Returns a sample JSON resource |
| POST | `/api/resource` | Creates a new resource (expects JSON) |
| PUT | `/api/resource/<id>` | Updates a resource |
| DELETE | `/api/resource/<id>` | Deletes a resource |

## Credibility & Maintainability Notes

- **Thread Separation:** The Flask server runs in a daemon thread, ensuring the GUI remains responsive.
- **Configuration Centralization:** All file paths, ports, and keys are managed in `config.py`.
- **Extensible API Layout:** `apis.py` is structured for modular route expansion without cluttering `appserver.py`.
- **Windows Compatibility:** Paths use backslashes (`\\`) and `os.chdir` ensures relative paths work correctly.

## Known Issues / Areas for Improvement

1. **`windows.py` is currently incomplete** – The port assignment logic contains errors (`url.port(config[...])` is invalid). Use `myapp.py` instead.
2. **PHP Server Integration:** The command in `start_server()` launches a blocking PHP server. Consider using `subprocess.Popen` instead of `os.system` for better control.
3. **No Live Reload:** Changes to backend code require a full restart.
4. **Security:** The `passKey` in `config.py` is hardcoded – move to environment variables for production.

## Contribution Guidelines

If you wish to continue development:

1. **Start with `whatsNext.txt`** – This is your prioritized roadmap.
2. **Refactor server management** – Replace `os.system` with `subprocess.Popen` and implement graceful shutdown.
3. **Add environment modes** – Implement `devMode` vs `usermode` to toggle debug features.
4. **Implement local database layer** – Use SQLite or TinyDB for persistent storage without external dependencies.

## License

(Include your license here – e.g., MIT, GPL, etc.)

## Acknowledgments

This project is built on:
- [Flask](https://flask.palletsprojects.com/)
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- [Qt WebEngine](https://doc.qt.io/qt-5/qtwebengine-index.html)

---

**Project Lead / Architect:** LiderWally

**Last Updated:** 31/01/2026

**For inquiries or contributions:** wawakowero11@gmail.com