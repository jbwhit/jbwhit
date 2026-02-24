# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///
from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(
    "🙂 [link=https://jonathanwhitmore.com]Jonathan Whitmore[/]"
    " — [bright_black]physicist, data scientist, generative artist",
    guide_style="bold bright_black",
)

talks_tree = tree.add("🎙️ Talks & Tutorials", guide_style="bright_black")
talks_tree.add(
    "[bold link=https://github.com/jbwhit/jupyter-tips-and-tricks]jupyter-tips-and-tricks[/]       - [bright_black]using Jupyter for data science"
)
talks_tree.add(
    "[bold link=https://github.com/jbwhit/OSCON-2015]OSCON-2015[/]                     - [bright_black]talk on Jupyter workflows"
)
talks_tree.add(
    "[bold link=https://github.com/jbwhit/2017-05-PyCon-EDA-Tutorial]PyCon EDA Tutorial[/]            - [bright_black]exploratory data analysis workshop"
)
talks_tree.add(
    "[bold link=https://github.com/jbwhit/2018-grace-hopper-eda-workshop]Grace Hopper Workshop[/]          - [bright_black]EDA workshop materials"
)

teaching_tree = tree.add("📚 Teaching", guide_style="bright_black")
teaching_tree.add(
    "[bold link=https://github.com/jbwhit/berkeley-jupyter-notebook]berkeley-jupyter-notebook[/]      - [bright_black]lecture at Berkeley Institute for Data Science"
)
teaching_tree.add(
    "[bold link=https://github.com/jbwhit/data-science-teams]data-science-teams[/]             - [bright_black]notebooks for my data science course"
)
teaching_tree.add(
    "[bold link=https://github.com/jbwhit/WSP-312-Tips-and-Tricks]WSP-312 Stanford[/]               - [bright_black]tips & tricks for data scientists (Stanford)"
)
teaching_tree.add(
    "[bold link=https://jbwhitmore.gumroad.com/l/jupytermastery]Jupyter Mastery[/]                - [bright_black]online course on mastering Jupyter"
)

projects_tree = tree.add("🔧 Projects", guide_style="bright_black")
projects_tree.add(
    "[bold link=https://jonathanwhitmore.com/projects/physics-quals/]UCSD Physics Quals Archive[/]     - [bright_black]PhD qualifying exams (1987-2019), maintained since 2008"
)
projects_tree.add(
    "[bold link=https://jonathanwhitmore.com/projects/checklists/]Decision Checklists[/]            - [bright_black]checklists for investing and causal inference"
)
projects_tree.add(
    "[bold link=https://github.com/jbwhit/lithuanianquiz]lithuanianquiz[/]                - [bright_black]FastHTML & MonsterUI webapp for learning Lithuanian"
)
projects_tree.add(
    "[bold link=https://github.com/jbwhit/RebalanceAssetAllocation]RebalanceAssetAllocation[/]       - [bright_black]Python code for portfolio allocation analysis"
)
projects_tree.add(
    "[bold link=https://github.com/jbwhit/fine-structure-inference]fine-structure-inference[/]       - [bright_black]data science methods for physics research"
)

online_tree = tree.add("⭐ Online", guide_style="bright_black")
online_tree.add(
    "[bold link=https://jonathanwhitmore.com]jonathanwhitmore.com[/]          - [bright_black]physics, data science, and learning systems"
)
online_tree.add(
    "[bold link=https://www.jbwhitmoreart.com/]jbwhitmoreart.com[/]             - [bright_black]generative art — motion, form, and color"
)
online_tree.add(
    "[bold link=https://www.youtube.com/@JonathanWhitmore]YouTube[/]                       - [bright_black]educational videos and live coding"
)

console.print(tree)
console.print("")
console.print(
    "[green]Find me on [bold link=https://x.com/jbwhitmore]@jbwhitmore[/]"
    " · [bold link=https://www.linkedin.com/in/jonathanbwhitmore/]LinkedIn[/]"
)

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
