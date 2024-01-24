# static-tex
Compiles LaTeX files using the [plasTeX compiler](https://github.com/plastex/plastex) and serves them as static HTML pages.
## Usage
1. Clone the repo: ```git clone https://github.com/hfjallborg/static-tex.git```
2. Install the dependencies: ```pip install -r requirements.txt```
3. Put all your .tex source files in the included `source` folder.
     * Your .tex files must have valid slugs as filenames (lowercase letters, digits and hyphens)
5. Run the build command: ```python -m static_tex build```
6. (Optional) run the built in server: ```python -m static_tex runserver```
