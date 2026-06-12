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
        "GPS in Reverse",
        "https://jbwhit.github.io/clocks/",
        "gravitational time dilation + particle-filter inference",
    )
)
projects_tree.add(
    entry(
        "The Rediscovery of Neptune",
        "https://jbwhit.github.io/discoverneptune/",
        "recreating Le Verrier's 1846 discovery with REBOUND",
    )
)
projects_tree.add(
    entry(
        "The Last Moon",
        "https://jbwhit.github.io/habitable-zone-black-holes/",
        "habitable-zone black holes as a technosignature",
    )
)
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
