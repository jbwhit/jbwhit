# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///
from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

LABEL_WIDTH = 30


def entry(label: str, url: str, desc: str) -> str:
    return f"[bold link={url}]{label}[/]{' ' * (LABEL_WIDTH - len(label))} - [bright_black]{desc}"


tree = Tree(
    "🙂 [link=https://jonathanwhitmore.com]Jonathan Whitmore[/]"
    " — [bright_black]physicist, data scientist, generative artist",
    guide_style="bold bright_black",
)

projects_tree = tree.add("🔧 Projects", guide_style="bright_black")
projects_tree.add(
    entry(
        "Lithuanian Practice",
        "https://lithuanian-practice.com/",
        "FastHTML & MonsterUI webapp for learning Lithuanian",
    )
)
projects_tree.add(
    entry(
        "UCSD Physics Quals Archive",
        "https://jonathanwhitmore.com/projects/physics-quals/",
        "PhD qualifying exams (1987-2019), maintained since 2008",
    )
)
projects_tree.add(
    entry(
        "Decision Checklists",
        "https://jonathanwhitmore.com/projects/checklists/",
        "checklists for investing and causal inference",
    )
)
projects_tree.add(
    entry(
        "RebalanceAssetAllocation",
        "https://github.com/jbwhit/RebalanceAssetAllocation",
        "Python code for portfolio allocation analysis",
    )
)
projects_tree.add(
    entry(
        "fine-structure-inference",
        "https://github.com/jbwhit/fine-structure-inference",
        "data science methods for physics research",
    )
)

teaching_tree = tree.add("📚 Teaching", guide_style="bright_black")
teaching_tree.add(
    entry(
        "berkeley-jupyter-notebook",
        "https://github.com/jbwhit/berkeley-jupyter-notebook",
        "lecture at Berkeley Institute for Data Science",
    )
)
teaching_tree.add(
    entry(
        "data-science-teams",
        "https://github.com/jbwhit/data-science-teams",
        "notebooks for my data science course",
    )
)
teaching_tree.add(
    entry(
        "WSP-312 Stanford",
        "https://github.com/jbwhit/WSP-312-Tips-and-Tricks",
        "tips & tricks for data scientists (Stanford)",
    )
)
teaching_tree.add(
    entry(
        "Jupyter Mastery",
        "https://jbwhitmore.gumroad.com/l/jupytermastery",
        "online course on mastering Jupyter",
    )
)

talks_tree = tree.add("🎙️ Talks & Tutorials", guide_style="bright_black")
talks_tree.add(
    entry(
        "Full talk archive",
        "https://jonathanwhitmore.com/projects/talks/",
        "conference talks, tutorials, and lectures (2011-2019)",
    )
)
talks_tree.add(
    entry(
        "jupyter-tips-and-tricks",
        "https://github.com/jbwhit/jupyter-tips-and-tricks",
        "using Jupyter for data science",
    )
)
talks_tree.add(
    entry(
        "OSCON-2015",
        "https://github.com/jbwhit/OSCON-2015",
        "talk on Jupyter workflows",
    )
)
talks_tree.add(
    entry(
        "PyCon EDA Tutorial",
        "https://github.com/jbwhit/2017-05-PyCon-EDA-Tutorial",
        "exploratory data analysis workshop",
    )
)
talks_tree.add(
    entry(
        "Grace Hopper Workshop",
        "https://github.com/jbwhit/2018-grace-hopper-eda-workshop",
        "EDA workshop materials",
    )
)

online_tree = tree.add("⭐ Online", guide_style="bright_black")
online_tree.add(
    entry(
        "jonathanwhitmore.com",
        "https://jonathanwhitmore.com",
        "physics, data science, and learning systems",
    )
)
online_tree.add(
    entry(
        "jbwhitmoreart.com",
        "https://www.jbwhitmoreart.com/",
        "generative art — motion, form, and color",
    )
)
online_tree.add(
    entry(
        "YouTube",
        "https://www.youtube.com/@JonathanWhitmore",
        "educational videos and live coding",
    )
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
