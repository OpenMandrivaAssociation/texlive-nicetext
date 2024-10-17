Name:		texlive-nicetext
Epoch:		1
Version:	38914
Release:	2
Summary:	Minimal markup for simple text (Wikipedia style) and documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nicetext
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicetext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicetext.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicetext.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle offers "minimal" markup syntax for various simple
kinds of text. The user will typically involve little more than
is printed, and will still get LaTeX quality. The bundle
provides four packages: - wiki addresses general texts, marked
up in the simple style used on Wikipedia; - niceverb is yet
another means of documenting LaTeX packages: it offers syntax-
aware typesetting of meta-variables (macro arguments) and for
referring to commands (and their syntax) in footnotes, section
titles etc.; - fifinddo aims to parse plain text or (La)TeX
files using TeX, and to write the results to an external file;
the package is used by another member of the bundle: - makedoc,
which provides the means to produce typeset documentation
direct from package files.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nicetext
%doc %{_texmfdistdir}/doc/latex/nicetext
#- source
%doc %{_texmfdistdir}/source/latex/nicetext

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
