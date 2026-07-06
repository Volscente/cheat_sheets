To set up a work environment that feels like a "Data Scientist turned Full-Stack Engineer," we should focus on **Developer Experience (DX)**. You want your tools to catch errors before you run the code and automate the boring stuff (like formatting).

---

## 1. VSCode: The "Pro-Stack" Configuration

For a Python/Next.js monorepo, you need extensions that understand both worlds.

### Essential Extensions

* **Python Pack:**
* **Python (Microsoft):** The baseline.
* **Pylance:** For incredibly fast type-checking and "IntelliSense" (crucial for SQLModel).
* **Ruff:** (Highly Recommended) In 2026, Ruff has replaced Flake8/Black. It’s an extremely fast Python linter and formatter written in Rust.


* **Web Development:**
* **ESLint & Prettier:** For Javascript/Typescript quality and auto-formatting.
* **Tailwind CSS IntelliSense:** Essential for the "Notion-look." It shows you color previews and autocompletes CSS classes.
* **Error Lens:** Instead of hovering over red lines, this prints the error message directly in the code line. It’s a game-changer for speed.


* **Productivity & Data:**
* **Thunder Client / REST Client:** Like Postman, but inside VSCode. Perfect for testing your FastAPI endpoints.
* **Docker:** To manage your PostgreSQL container without leaving the IDE.



### Recommended `settings.json`

To make VSCode behave, press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Win), type "Open User Settings (JSON)", and add/update these:

```json
{
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll": "explicit",
        "source.organizeImports": "explicit"
    },
    "python.analysis.typeCheckingMode": "basic", // Helps catch SQLModel errors early
    "tailwindCSS.emmetCompletions": true,
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff"
    },
    "[typescriptreact]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    }
}

```

---

## 2. GitHub: The Monorepo Strategy

For a solo project, you don't need complex tools like Turborepo yet, but a clean structure is vital.

### The Directory Structure

Create one root folder and divide it clearly:

```text
/german-vocab-app
│── /backend          # FastAPI + SQLModel + Dockerfile
│── /frontend         # Next.js + Tailwind + Dockerfile
│── /data             # (Optional) For CSVs or initial datasets
│── docker-compose.yml
│── .gitignore
└── README.md

```

### GitHub Configuration Tips

1. **The `.gitignore`:** Ensure you have a "Global" gitignore that includes both `.venv` (Python) and `node_modules` (JS), plus `.env` files where you'll eventually store your LLM API keys.
2. **GitHub Projects:** Since we have our Sprint plan, I recommend using the **"Projects"** tab on your GitHub repo.
* Create a "Board" view.
* Add our Sprints as "Columns" or "Milestones."
* It helps you stay focused so you don't start the LLM part before the DB is working.


3. **Branching:** Even if it's just you, work on branches (e.g., `feat/db-setup`, `feat/frontend-table`). It makes it much easier to roll back if a library update breaks everything.

---

## 3. Sparring Check: Virtual Environments

Since you're a Data Scientist, you might use **Conda**. For web dev, I suggest sticking to **`venv`** or **`Poetry`** inside the `/backend` folder. It keeps the Docker build much smaller and faster than Conda.

**Are you ready to initialize the repository? I can give you the specific commands to create this structure and the `.gitignore` to get started.**


Great questions. Let's get precise. In the world of software development, names matter because they are the "keys" to the tools we use.

### 1. VSCode Extension "Key" Names

The Marketplace search is a bit picky. Here are the exact **Publisher + Name** identifiers. You can paste these into the VSCode extension search bar:

* **`ms-python.python`**: (Official name: **Python**) — This is the one from Microsoft. It will also prompt you to install **Pylance** and **Python Debugger**, which you should accept.
* **`ms-python.vscode-pylance`**: (**Pylance**) — For fast type-checking.
* **`charliermarsh.ruff`**: (**Ruff**) — This is the lightning-fast linter/formatter I mentioned.
* **`bradlc.vscode-tailwindcss`**: (**Tailwind CSS IntelliSense**) — Essential for the UI phase.
* **`esbenp.prettier-vscode`**: (**Prettier**) — Code formatter for your Next.js/React code.
* **`usernamehw.errorlens`**: (**Error Lens**) — Displays errors inline so you don't have to hover.
* **`ms-azuretools.vscode-docker`**: (**Docker**) — To manage your containers.

---

### 2. Branch Naming & "feat"

The "feat" stands for **Feature**. This comes from the **Conventional Commits** standard, which is the industry gold standard for keeping a clean history.

When you see `feat/db-setup`, it tells anyone (or your future self) exactly what kind of work is inside that branch. Here is the standard prefix list:

| Prefix | Use Case |
| --- | --- |
| **`feat/`** | New features (e.g., `feat/add-login`, `feat/llm-integration`). |
| **`fix/`** | Bug fixes (e.g., `fix/typo-in-german-word`). |
| **`docs/`** | Documentation only changes (e.g., `docs/update-readme`). |
| **`refactor/`** | Code changes that neither fix a bug nor add a feature (cleaning up code). |
| **`chore/`** | Updating dependencies, build scripts, or configurations. |

**Pro-tip:** Use hyphens, not spaces or underscores (e.g., `feat/ui-filters`). It's safer for CLI tools.

---

### 3. Using `uv` (The Data Scientist's Choice)

Yes! You **should** use `uv` instead of Poetry. It is written in Rust, significantly faster, and handles Python version management natively.

#### Where to init?

Since we are doing a **monorepo**, the best way to use `uv` is via **Workspaces**. This allows you to have one shared lockfile at the root, ensuring all your "sub-projects" (like `/backend`) are compatible, but keeps their code separate.

**Recommended Setup Command:**

1. Create your root folder: `mkdir german-vocab-app && cd german-vocab-app`
2. Initialize the workspace: `uv init --workspace`
3. Add the backend as a member: `uv init --package backend`

This creates a `pyproject.toml` in the root that looks like this:

```toml
[tool.uv.workspace]
members = ["backend"]

```

This way, you can run `uv run --package backend uvicorn main:app` from the **root** of your project, but your FastAPI code stays neatly tucked inside the `/backend` folder.

**Would you like the exact folder structure and the initial `.gitignore` file to copy-paste into your new repo?**


To wrap up your environment setup, let's get you tuned for high-speed coding and professional debugging.

### 1. Enabling and Using Plugins

Extensions in VSCode are usually "auto-enabled" as soon as you hit **Install**. However, for a professional workflow, you don't just "have" them—you "summon" them.

* **To search and install:** `Cmd + Shift + X` (Mac) or `Ctrl + Shift + X` (Win).
* **To configure:** Most extensions contribute settings. Press `Cmd + ,` (Comma) to open the Settings UI and search for the extension name (e.g., "Ruff").
* **To use specific commands:** Press `Cmd + Shift + P` (The Command Palette) and type the name of the extension.
* *Example:* Type `Ruff: Fix all auto-fixable problems` to clean up your Python file instantly.



---

### 2. Python Debugging: The "Magic Pause Button"

Since you're a Data Scientist, you might be used to `print()` statements. In software dev, we use the **Debugger** to freeze time and inspect variables without re-running scripts.

#### The "No-Config" Way (Quick Start)

1. Open a `.py` file.
2. Click in the **margin (gutter)** to the left of a line number. A **Red Dot** (Breakpoint) will appear.
3. Press **`F5`**.
4. Select "Python Debugger: Python File". The code will run and stop exactly at your red dot.

#### The "Pro" Way (`launch.json`)

Since we are building a FastAPI app, you don't want to just run a script; you want to debug the **Server**.

1. Go to the **Run and Debug** tab (`Cmd + Shift + D`).
2. Click **"create a launch. json file"**.
3. Choose **FastAPI**. VSCode will generate a config that looks like this:

```json
{
 "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "fetch-gms-validations: single entity",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/menu_digitalisation_service/mds/utils/gms_integration/fetch_gms_validations.py",
      "args": ["--global-entity-id", "FP_HK"],
      "console": "integratedTerminal",
      "envFile": "${workspaceFolder}/menu_digitalisation_service/mds/.env"
    },
    {
      "name": "fetch-gms-validations: dry-run single entity",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/menu_digitalisation_service/mds/utils/gms_integration/fetch_gms_validations.py",
      "args": ["--global-entity-id", "FP_HK", "--dry-run"],
      "console": "integratedTerminal",
      "envFile": "${workspaceFolder}/menu_digitalisation_service/mds/.env"
    },
    {
      "name": "fetch-gms-validations: all entities",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/menu_digitalisation_service/mds/utils/gms_integration/fetch_gms_validations.py",
      "args": ["--all"],
      "console": "integratedTerminal",
      "envFile": "${workspaceFolder}/menu_digitalisation_service/mds/.env"
    }
  ]
}

```

Now, whenever you hit **`F5`**, your server starts, and you can "catch" requests as they come in from your frontend!

---

### 3. Essential "Power User" Commands

| Plugin / Tool | Key Command | Action |
| --- | --- | --- |
| **Command Palette** | `Cmd + Shift + P` | The "God Mode" search. Use this for everything. |
| **Quick Open** | `Cmd + P` | Search for any file in your monorepo instantly. |
| **Ruff (Linting)** | `Shift + Alt + F` | Formats your Python code to professional standards. |
| **Docker** | Click Docker Icon | Start/Stop your PostgreSQL container with one click. |
| **Error Lens** | (Automatic) | Errors will appear as text at the end of the line. |

---

### Summary Checklist for your "Workspace Setup"

* [ ] **VSCode Plugins installed** via `Cmd+Shift+X`.
* [ ] **GitHub Repo initialized** with `uv init --workspace`.
* [ ] **`.gitignore` created** (to hide `node_modules` and `.venv`).
* [ ] **`launch.json` created** for FastAPI debugging.

**You’re now fully equipped.** **Shall we move to Phase 1: Sprint 1 and write the actual `docker-compose.yml` and the first Python models?**


Coding is as much about vibe as it is about logic. If your environment looks like a "hacker terminal from 2026," you'll likely enjoy those long debugging sessions a lot more.

Here are the best aesthetic customizations to make your VSCode look clean, modern, and distinctively "Data Scientist":

### 1. The "Big Three" Themes

Search for these in the Extensions marketplace (`Cmd + Shift + X`):

* **Catppuccin**: (My top pick) It’s famous for having soft, pastel colors that are incredibly easy on the eyes. It comes in four "flavors": Latte (Light), Frappé, Macchiato, and Mocha (Darkest).
* **Tokyo Night**: Inspired by the neon lights of Tokyo at night. It uses deep blues and purples with sharp, glowing accents.
* **GitHub Theme**: If you like the clean look of the GitHub website, "GitHub Dark Dimmed" is a professional, low-contrast favorite.

### 2. High-End Typography

A good coding font makes a massive difference. You want a **Monospaced** font with **Ligatures** (which turn `->` into a sleek arrow symbol ).

* **Fira Code**: The most popular open-source choice.
* **JetBrains Mono**: Extremely readable, specifically designed for developers.
* **Cascadia Code**: Microsoft’s modern font (often comes pre-installed, but you need to enable ligatures).

**How to enable them:**

1. Install the font on your computer.
2. In VSCode `settings.json`, add:
```json
"editor.fontFamily": "'JetBrains Mono', 'Fira Code', monospace",
"editor.fontLigatures": true,

```



### 3. Icon Themes

Standard folder icons are boring. Install one of these to make your file tree look like a professional project:

* **Material Icon Theme**: The industry standard. It has specific icons for everything (FastAPI, Docker, React, etc.).
* **Catppuccin Icons**: If you use the Catppuccin theme, these icons match the pastel color palette perfectly.

### 4. Layout "De-cluttering"

To get that minimal "Notion" or "Zen" look, try these UI tweaks in your settings:

* **Hide the Activity Bar**: Right-click the sidebar icons and select "Move Activity Bar to Top" or "Hide."
* **Centered Layout**: Press `Cmd + Shift + P` and type "Toggle Centered Layout" when you want to focus on just one file in the middle of your screen.
* **Sticky Scroll**: This keeps the function or class name at the top of the editor as you scroll.
```json
"editor.stickyScroll.enabled": true

```



### 5. The "Data Scientist" Bonus: Indent Rainbow

Search for **`oderwat.indent-rainbow`**. It subtly colors the indentation levels of your code. For Python (where indentation is everything), it’s not just aesthetic—it’s a functional safeguard against "indentation errors."

---

### Final "Aesthetic" Settings Block

Copy this into your `settings.json` for an immediate glow-up:

```json
{
  "workbench.colorTheme": "Catppuccin Mocha",
  "workbench.iconTheme": "material-icon-theme",
  "editor.cursorStyle": "line",
  "editor.cursorBlinking": "expand",
  "editor.minimap.enabled": false, // Hides the tiny map on the right for a cleaner look
  "workbench.startupEditor": "none",
  "editor.lineHeight": 22, // Adds a bit of "breathing room" to your code
  "editor.guides.indentation": true,
  "editor.renderLineHighlight": "all"
}

```

**How do you like these suggestions? If your environment feels ready, shall we finally dive into Phase 1, Sprint 1 and build the Docker/FastAPI skeleton?**


To get that perfect 2026 developer look, follow these specific steps. Since you're on a Mac (based on your screenshot), I've tailored the commands for macOS.

### 1. Install & Setup Catppuccin Theme

This is the "skin" of your editor.

1. **Install:** Open the Extensions view (`Cmd + Shift + X`), search for **"Catppuccin for VSCode"** (published by Catppuccin), and click **Install**.
2. **Activate:** Once installed, a menu should pop up automatically. If not, press `Cmd + Shift + P`, type **"Color Theme"**, and select it.
3. **Choose your Flavor:** You will see four options. I recommend **Catppuccin Mocha** for a sleek, dark aesthetic.
4. **Extra Polish:** Open your `settings.json` (`Cmd + Shift + P` -> "Open User Settings (JSON)") and add this to make the terminal colors match perfectly:
```json
"terminal.integrated.minimumContrastRatio": 1,
"editor.semanticHighlighting.enabled": true

```



---

### 2. Install JetBrains Mono & Enable Ligatures

This is the font. It’s famous for making code more readable and turning symbols like `!=` into a single  glyph.

1. **Download:** Go to the [official JetBrains Mono page](https://www.jetbrains.com/lp/mono/) and click **Download font**.
2. **Install on Mac:** * Unzip the folder.
* Open the `fonts/ttf` folder.
* Select all `.ttf` files, right-click, and select **Open with Font Book**.
* Click **Install**.


3. **Configure VSCode:** Open your `settings.json` and add/update these lines:
```json
"editor.fontFamily": "'JetBrains Mono', monospace",
"editor.fontLigatures": true,
"editor.fontSize": 13,
"editor.lineHeight": 22 

```


*Note: You must restart VSCode completely (Quit and Re-open) for the new font to register.*

---

### 3. Install & Setup Catppuccin Icons

This changes the file icons in your sidebar to match the theme's colors.

1. **Install:** Search the Extensions view for **"Catppuccin Icons for VSCode"** (published by Catppuccin) and click **Install**.
2. **Activate:** Press `Cmd + Shift + P`, type **"File Icon Theme"**, and select **Catppuccin Mocha** (or whichever flavor you chose for the main theme).
3. **Customization:** If you want to change specific folder colors later, you can find the settings under **Settings > Extensions > Catppuccin Icons**.

---

### The "Final Look" Result

Once you’ve done this, your VSCode will have a soft, cohesive pastel palette, high-readability typography, and distinct icons for your Python and React files.

**How does it look? If you're happy with the vibe, would you like to start on Phase 1, Sprint 1: Setting up the Dockerized Backend and Database?**


Ah, I see what's happening. The `catppuccin.accentColor` setting is actually designed to accept a **string keyword** (like "mauve", "green", "lavender") from the official Catppuccin palette, rather than a raw Hex code. When you put a Hex code there, the extension doesn't recognize it and falls back to the default blue.

To use your specific dark green (`#2d6a4f`), you have two ways to do it.

### Method 1: The "Custom UI Colors" Way (Recommended)

This is the most reliable way to inject a specific Hex code into the UI elements that usually follow the accent color. In your `settings.json`, add this block:

```json
"catppuccin.customUIColors": {
    "all": {
        "accent": "#2d6a4f"
    }
}

```

*Note: You may need to run the command `Developer: Reload Window` from the Command Palette (`Cmd+Shift+P`) for this to take effect.*

---

### Method 2: Overriding a Palette Color

If you want to "hijack" one of the existing names (for example, if you set your accent to "green" but want it to be *your* specific green), you can override the palette:

1. Set the accent to a name: `"catppuccin.accentColor": "green"`
2. Override what "green" means:

```json
"catppuccin.colorOverrides": {
    "all": {
        "green": "#2d6a4f"
    }
}

```

---

### Method 3: The GUI Customizer

If you want to see the changes live without guessing JSON keys, the Catppuccin team actually built a custom UI for this:

1. Open the Command Palette (`Cmd+Shift+P`).
2. Type **"Catppuccin: Customize Theme"**.
3. This opens a visual dashboard where you can play with colors and see them update in real-time.

### A Note on your chosen color `#2d6a4f`

Since you're a Data Scientist, you likely appreciate the "visual contrast" aspect. That green is quite dark. If you find that the UI text or icons become hard to see against the dark background of Catppuccin Mocha, you might want to try a slightly brighter version of that green (like `#40916c`) for the accent, as accents are usually used for thin lines and small highlights.

**Does that solve the color reset issue for you? If so, are we ready to jump into the code for Phase 1, Sprint 1?**


## Settings
```
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit",
    "source.organizeImports": "explicit",
  },
  "editor.stickyScroll.enabled": true,
  "python.analysis.typeCheckingMode": "basic", // Helps catch SQLModel errors early
  "tailwindCSS.emmetCompletions": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
  },
  "workbench.activityBar.location": "top",
  "editor.cursorStyle": "line",
  "editor.cursorBlinking": "expand",
  "editor.minimap.enabled": false, // Hides the tiny map on the right for a cleaner look
  "workbench.startupEditor": "none",
  "editor.guides.indentation": true,
  "editor.renderLineHighlight": "all",
  "terminal.integrated.minimumContrastRatio": 1,
  "editor.semanticHighlighting.enabled": true,
  "editor.fontFamily": "'JetBrains Mono', monospace",
  "editor.fontLigatures": true,
  "editor.fontSize": 13,
  "editor.lineHeight": 22,
  "workbench.colorTheme": "Catppuccin Mocha",
  // Using the light mode
  "indentRainbow.indicatorStyle": "light",
  // we use a simple 1 pixel wide line
  "indentRainbow.lightIndicatorStyleLineWidth": 1,
  // the same colors as above but more visible
  "indentRainbow.colors": [
    "rgba(255,255,64,0.3)",
    "rgba(127,255,127,0.3)",
    "rgba(255,127,255,0.3)",
    "rgba(79,236,236,0.3)",
  ],
  "workbench.iconTheme": "catppuccin-mocha",
  "catppuccin.accentColor": "green_dark",
  "catppuccin.colorOverrides": {
    "all": {
      "green_dark": "#40916c",
    },
  },
}

```


## Problem Fix
### Testing with Docker-Compose

- Ensure to stop any PostgreSQL instance running on your local machine.
- Ensure to make the DATABASE_URL available in the .env file, like:

```
# .env
POSTGRES_USER=devuser
POSTGRES_PASSWORD=asdsa
POSTGRES_DB=vademecum
POSTGRES_HOST_LOCAL=localhost
POSTGRES_HOST_DOCKER=db
POSTGRES_PORT=5432

# Assemble the URL for local debugging (VS Code / Pytest)
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST_LOCAL}:${POSTGRES_PORT}/${POSTGRES_DB}
```

- Add a `.vscode/settings.json`:
```json
{
  "python.testing.pytestArgs": ["backend/tests"],
  "python.testing.unittestEnabled": false,
  "python.testing.pytestEnabled": true,
  "python.envFile": "${workspaceFolder}/.env",
  "python.testing.pytestPath": "pytest"
}
```
- Ensure that the database is running as docker-compose service
```yml
services:
  db:
    image: postgres:15-alpine
    container_name: vademecum_db
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "${POSTGRES_PORT}:5432"
```
```bash
# The name of the service you can find in docker-compose.yml
docker-compose up -d db
```
