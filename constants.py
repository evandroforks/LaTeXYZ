import urllib.request
import re


def tidy(x):
    if "{}" in x:
        y = x.replace("\\", "")
        y = y.replace("{}{}", "{$1}{$2}")
        y = y.replace("{}", "{$1}")
        return (x, y)
    else:
        return (x, )


def existed(x, existing):
    for c in existing:
        if x.strip("\\{}") == c[0].strip("\\{}"):
            return True
    return False


def generate_symbols(url, a="^", b="$", existing_commands=[]):
    response = urllib.request.urlopen(url)
    webContent = response.read().decode("utf8")
    m = re.search(a, webContent)
    m2 = re.search(b, webContent)
    webContent = webContent[m.span()[1]:m2.span()[0]]
    items = list(set(re.findall(r"\\[a-zA-Z]{2,}(?:(?:\{\})+)?", webContent)))
    return [tidy(item) for item in items if not existed(item, existing_commands)]


_math_commands = [
    ("\\alpha", ),
    ("\\beta", ),
    ("\\gamma", ),
    ("\\delta", ),
    ("\\epsilon", ),
    ("\\varepsilon", ),
    ("\\zeta", ),
    ("\\eta", ),
    ("\\theta", ),
    ("\\vartheta", ),
    ("\\iota", ),
    ("\\kappa", ),
    ("\\varkappa", ),
    ("\\lambda", ),
    ("\\mu", ),
    ("\\nu", ),
    ("\\xi", ),
    ("\\pi", ),
    ("\\rho", ),
    ("\\varrho", ),
    ("\\sigma", ),
    ("\\varsigma", ),
    ("\\tau", ),
    ("\\upsilon", ),
    ("\\phi", ),
    ("\\varphi", ),
    ("\\chi", ),
    ("\\psi", ),
    ("\\omega", ),
    ("\\digamma", ),
    ("\\Gamma", ),
    ("\\Delta", ),
    ("\\Theta", ),
    ("\\Lambda", ),
    ("\\Xi", ),
    ("\\Pi", ),
    ("\\Sigma", ),
    ("\\Phi", ),
    ("\\Psi", ),
    ("\\Omega", ),

    ("\\big", ),
    ("\\Big", ),
    ("\\bigg", ),
    ("\\Bigg", ),
    ("\\quad", ),
    ("\\qquad", ),
    ("\\nonumber", ),

    ("\\bigcup", ),
    ("\\bigcap", ),

    ("\\mathnormal", ),
    ("\\mathrm", ),
    ("\\mathit", ),
    ("\\mathbf", ),
    ("\\mathsf", ),
    ("\\mathtt", ),
    ("\\mathfrak", ),
    ("\\mathcal", ),
    ("\\mathbb", ),
    ("\\mathscr", ),
    ("\\text{}", "text{$1}"),

    ("\\hat", ),
    ("\\bar", ),
    ("\\tilde", ),
    ("\\widehat{}", "widehat{$1}"),
    ("\\widetilde{}", "widetilde{$1}"),
    ("\\overbrace{}{}", "overbrace{$1}{$2}"),
    ("\\underbrace{}{}", "underbrace{$1}{$2}"),
    ("\\overrightarrow{}", "overrightarrow{$1}"),
    ("\\overleftarrow{}", "overleftarrow{$1}"),

    ("\\sum_{}^{}", "sum_{$1}^{$2}"),
    ("\\prod_{}^{}", "prod_{$1}^{$2}"),
    ("\\int_{}^{}", "int_{$1}^{$2}"),
    ("\\iint_{}^{}", "iint_{$1}^{$2}"),
    ("\\iiint_{}^{}", "iiint_{$1}^{$2}"),
    ("\\iiiint_{}^{}", "iiiint_{$1}^{$2}"),
    ("\\idotsint{}^{}", "idotsint{$1}^{$2}"),
    ("\\oint_{}^{}", "oint_{$1}^{$2}"),

    ("\\frac{}{}", "frac{$1}{$2}"),
    ("\\binom{}{}", "binom{$1}{$2}"),
    ("\\overset{}{}", "overset{$1}{$2}"),
    ("\\underset{}{}", "underset{$1}{$2}")
]

_general_commands = [
    ("\\usagepacage", ),
    ("\\includegraphics", ),
    ("\\part{}", "part{$1}"),
    ("\\part*{}", "part*{$1}"),
    ("\\chapter{}", "chapter{$1}"),
    ("\\chapter*{}", "chapter*{$1}"),
    ("\\section{}", "section{$1}"),
    ("\\section*{}", "section*{$1}"),
    ("\\subsection{}", "subsection{$1}"),
    ("\\subsection*{}", "subsection*{$1}"),
    ("\\subsubsection{}", "subsubsection{$1}"),
    ("\\subsubsection*{}", "subsubsection*{$1}"),

    ("\\underline{}", "underline{$1}"),
    ("\\overline{}", "overline{$1}"),

    ("\\bibliographystyle", ),
    ("\\bibliography", ),
    ("\\addbibresource", )
]

# generate_symbols('https://en.wikibooks.org/wiki/LaTeX/Mathematics',
#                  "Relation Symbols",
#                  "\\\\cis",
#                  _math_commands)

math_commands = _math_commands + [
    ('\\aleph',),
    ('\\amalg',),
    ('\\approx',),
    ('\\arccos',),
    ('\\arccot',),
    ('\\arcsin',),
    ('\\arctan',),
    ('\\ast',),
    ('\\asymp',),
    ('\\backslash',),
    ('\\beth',),
    ('\\bigcirc',),
    ('\\bigtriangledown',),
    ('\\bigtriangleup',),
    ('\\bot',),
    ('\\bowtie',),
    ('\\Box',),
    ('\\bullet',),
    ('\\cap',),
    ('\\cdot',),
    ('\\circ',),
    ('\\cong',),
    ('\\cos',),
    ('\\cosh',),
    ('\\cot',),
    ('\\coth',),
    ('\\csc',),
    ('\\cup',),
    ('\\dagger',),
    ('\\dashv',),
    ('\\ddagger',),
    ('\\diamond',),
    ('\\displaystyle',),
    ('\\div',),
    ('\\doteq',),
    ('\\Downarrow',),
    ('\\downarrow',),
    ('\\ell',),
    ('\\emptyset',),
    ('\\equiv',),
    ('\\eth',),
    ('\\exists',),
    ('\\forall',),
    ('\\frown',),
    ('\\geq',),
    ('\\gets',),
    ('\\gg',),
    ('\\gimel',),
    ('\\hbar',),
    ('\\iff',),
    ('\\Im',),
    ('\\imath',),
    ('\\implies',),
    ('\\in',),
    ('\\infty',),
    ('\\jmath',),
    ('\\land',),
    ('\\langle',),
    ('\\lceil',),
    ('\\leftarrow',),
    ('\\Leftrightarrow',),
    ('\\leftrightarrow',),
    ('\\leq',),
    ('\\lfloor',),
    ('\\ll',),
    ('\\lor',),
    ('\\mapsto',),
    ('\\measuredangle',),
    ('\\mid',),
    ('\\models',),
    ('\\mp',),
    ('\\nabla',),
    ('\\neg',),
    ('\\neq',),
    ('\\nexists',),
    ('\\ni',),
    ('\\notin',),
    ('\\nparallel',),
    ('\\nsubseteq',),
    ('\\nsupseteq',),
    ('\\odot',),
    ('\\ominus',),
    ('\\operatorname',),
    ('\\oplus',),
    ('\\oslash',),
    ('\\otimes',),
    ('\\parallel',),
    ('\\partial',),
    ('\\perp',),
    ('\\pm',),
    ('\\prec',),
    ('\\preceq',),
    ('\\propto',),
    ('\\rangle',),
    ('\\rceil',),
    ('\\Re',),
    ('\\rfloor',),
    ('\\Rightarrow',),
    ('\\rightarrow',),
    ('\\sec',),
    ('\\setminus',),
    ('\\sim',),
    ('\\simeq',),
    ('\\sin',),
    ('\\sinh',),
    ('\\smile',),
    ('\\sphericalangle',),
    ('\\sqcap',),
    ('\\sqcup',),
    ('\\sqsubset',),
    ('\\sqsubseteq',),
    ('\\sqsupset',),
    ('\\sqsupseteq',),
    ('\\star',),
    ('\\subset',),
    ('\\subseteq',),
    ('\\succ',),
    ('\\succeq',),
    ('\\supset',),
    ('\\supseteq',),
    ('\\tan',),
    ('\\tanh',),
    ('\\times',),
    ('\\to',),
    ('\\top',),
    ('\\triangleleft',),
    ('\\triangleright',),
    ('\\uparrow',),
    ('\\Uparrow',),
    ('\\uplus',),
    ('\\Upsilon',),
    ('\\varnothing',),
    ('\\varpi',),
    ('\\vdash',),
    ('\\vee',),
    ('\\wedge',),
    ('\\wp',),
    ('\\wr',)
]

# generate_symbols('https://en.wikibooks.org/wiki/LaTeX/Command_Glossary',
#                  "^",
#                  "$",
#                  math_commands + _general_commands)

general_commands = _general_commands + [
    ('\\addcontentsline',),
    ('\\address',),
    ('\\addtocontents',),
    ('\\addtocounter',),
    ('\\addtolength',),
    ('\\addvspace',),
    ('\\alph',),
    ('\\appendix',),
    ('\\arabic',),
    ('\\author',),
    ('\\author{}', 'author{$1}'),
    ('\\baselineskip',),
    ('\\baselinestretch',),
    ('\\bfseries',),
    ('\\bibitem',),
    ('\\bigskip',),
    ('\\bigskipamount',),
    ('\\boldmath',),
    ('\\boldsymbol',),
    ('\\cal',),
    ('\\caption',),
    ('\\cdots',),
    ('\\centering',),
    ('\\circle',),
    ('\\cite',),
    ('\\cleardoublepage',),
    ('\\clearpage',),
    ('\\cline',),
    ('\\closing',),
    ('\\color',),
    ('\\copyright',),
    ('\\dashbox',),
    ('\\date',),
    ('\\ddots',),
    ('\\documentclass',),
    ('\\dotfill',),
    ('\\em',),
    ('\\emph',),
    ('\\ensuremath',),
    ('\\epigraph',),
    ('\\euro',),
    ('\\fbox',),
    ('\\fill',),
    ('\\flushbottom',),
    ('\\fnsymbol',),
    ('\\footnote',),
    ('\\footnotemark',),
    ('\\footnotesize',),
    ('\\footnotetext',),
    ('\\frame',),
    ('\\framebox',),
    ('\\frenchspacing',),
    ('\\hfill',),
    ('\\hline',),
    ('\\href',),
    ('\\hrulefill',),
    ('\\hspace',),
    ('\\Huge',),
    ('\\huge',),
    ('\\hyphenation',),
    ('\\include',),
    ('\\includeonly',),
    ('\\indent',),
    ('\\input',),
    ('\\item',),
    ('\\itshape',),
    ('\\kill',),
    ('\\label',),
    ('\\LARGE',),
    ('\\large',),
    ('\\Large',),
    ('\\LaTeX',),
    ('\\LaTeXe',),
    ('\\ldots',),
    ('\\left',),
    ('\\lefteqn',),
    ('\\line',),
    ('\\linebreak',),
    ('\\linethickness',),
    ('\\linewidth',),
    ('\\listoffigures',),
    ('\\listoftables',),
    ('\\location',),
    ('\\makebox',),
    ('\\maketitle',),
    ('\\markboth',),
    ('\\markright',),
    ('\\mathop',),
    ('\\mbox',),
    ('\\medskip',),
    ('\\multicolumn',),
    ('\\multiput',),
    ('\\newcolumntype',),
    ('\\newcommand',),
    ('\\newcounter',),
    ('\\newenvironment',),
    ('\\newfont',),
    ('\\newlength',),
    ('\\newline',),
    ('\\newpage',),
    ('\\newsavebox',),
    ('\\newtheorem',),
    ('\\nocite',),
    ('\\noindent',),
    ('\\nolinebreak',),
    ('\\nonfrenchspacing',),
    ('\\nopagebreak',),
    ('\\normalsize',),
    ('\\not',),
    ('\\onecolumn',),
    ('\\opening',),
    ('\\oval',),
    ('\\pagebreak',),
    ('\\pagenumbering',),
    ('\\pageref',),
    ('\\pagestyle',),
    ('\\par',),
    ('\\paragraph',),
    ('\\parbox',),
    ('\\parindent',),
    ('\\parskip',),
    ('\\protect',),
    ('\\providecommand',),
    ('\\put',),
    ('\\raggedbottom',),
    ('\\raggedleft',),
    ('\\raggedright',),
    ('\\raisebox',),
    ('\\ref',),
    ('\\renewcommand',),
    ('\\right',),
    ('\\rmfamily',),
    ('\\roman',),
    ('\\rule',),
    ('\\savebox',),
    ('\\sbox',),
    ('\\scriptsize',),
    ('\\scshape',),
    ('\\setcounter',),
    ('\\setlength',),
    ('\\settowidth',),
    ('\\sffamily',),
    ('\\shortstack',),
    ('\\signature',),
    ('\\signature{}', 'signature{$1}'),
    ('\\slash',),
    ('\\slshape',),
    ('\\small',),
    ('\\smallskip',),
    ('\\sout',),
    ('\\space',),
    ('\\sqrt',),
    ('\\stackrel',),
    ('\\stepcounter',),
    ('\\subparagraph',),
    ('\\tableofcontents',),
    ('\\telephone',),
    ('\\TeX',),
    ('\\textbf{}', 'textbf{$1}'),
    ('\\textcolor{}{}', 'textcolor{$1}{$2}'),
    ('\\textheight',),
    ('\\textit{}', 'textit{$1}'),
    ('\\textmd{}', 'textmd{$1}'),
    ('\\textnormal{}', 'textnormal{$1}'),
    ('\\textrm{}', 'textrm{$1}'),
    ('\\textsc{}', 'textsc{$1}'),
    ('\\textsf{}', 'textsf{$1}'),
    ('\\textsl{}', 'textsl{$1}'),
    ('\\texttt{}', 'texttt{$1}'),
    ('\\textup{}', 'textup{$1}'),
    ('\\textwidth',),
    ('\\thanks',),
    ('\\thispagestyle',),
    ('\\tiny',),
    ('\\title',),
    ('\\title{}', 'title{$1}'),
    ('\\today',),
    ('\\ttfamily',),
    ('\\twocolumn',),
    ('\\typein',),
    ('\\typeout',),
    ('\\uline',),
    ('\\unitlength',),
    ('\\usebox',),
    ('\\usecounter',),
    ('\\uwave',),
    ('\\value',),
    ('\\vbox',),
    ('\\vcenter',),
    ('\\vdots',),
    ('\\vector',),
    ('\\verb',),
    ('\\vfill',),
    ('\\vline',),
    ('\\vphantom',),
    ('\\vspace',),
]


arrow_map = {
    "<-": "\\leftarrow",
    "<--": "\\longleftarrow",
    "->": "\\rightarrow",
    "-->": "\\longrightarrow",
    "<->": "\\leftrightarrow",
    "<-->": "\\longleftrightarrow",
    "<=": "\\Leftarrow",
    "<==": "\\Longleftarrow",
    "=>": "\\Rightarrow",
    "==>": "\\Longrightarrow",
    "<=>": "\\Leftrightarrow",
    "<==>": "\\Longleftrightarrow"
}
