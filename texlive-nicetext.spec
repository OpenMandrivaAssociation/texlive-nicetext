# revision 28423
# category Package
# catalog-ctan /macros/latex/contrib/nicetext
# catalog-date 2012-12-02 13:05:20 +0100
# catalog-license lppl
# catalog-version 0.65
Name:		texlive-nicetext
Epoch:		1
Version:	0.65
Release:	8
Summary:	Minimal markup for simple text (Wikipedia style) and documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nicetext
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicetext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicetext.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nicetext.source.tar.xz
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
%{_texmfdistdir}/tex/latex/nicetext/fifinddo.sty
%{_texmfdistdir}/tex/latex/nicetext/makedoc.cfg
%{_texmfdistdir}/tex/latex/nicetext/makedoc.sty
%{_texmfdistdir}/tex/latex/nicetext/mdoccorr.cfg
%{_texmfdistdir}/tex/latex/nicetext/nicetext.RLS
%{_texmfdistdir}/tex/latex/nicetext/niceverb.sty
%{_texmfdistdir}/tex/latex/nicetext/run/README-run.txt
%{_texmfdistdir}/tex/latex/nicetext/run/arseneau.tex
%{_texmfdistdir}/tex/latex/nicetext/run/atari.cfg
%{_texmfdistdir}/tex/latex/nicetext/run/atari.txt
%{_texmfdistdir}/tex/latex/nicetext/run/copyfile.cfg
%{_texmfdistdir}/tex/latex/nicetext/run/copyfile.tex
%{_texmfdistdir}/tex/latex/nicetext/run/fddial0g.sty
%{_texmfdistdir}/tex/latex/nicetext/run/fdtxttex.cfg
%{_texmfdistdir}/tex/latex/nicetext/run/fdtxttex.tex
%{_texmfdistdir}/tex/latex/nicetext/run/fdtxttex.tpl
%{_texmfdistdir}/tex/latex/nicetext/run/lines.txt
%{_texmfdistdir}/tex/latex/nicetext/run/makedoc.tpl
%{_texmfdistdir}/tex/latex/nicetext/run/sample.txt
%{_texmfdistdir}/tex/latex/nicetext/run/substr.tex
%{_texmfdistdir}/tex/latex/nicetext/run/u8atablg.fdf
%{_texmfdistdir}/tex/latex/nicetext/wiki.sty
%doc %{_texmfdistdir}/doc/latex/nicetext/ANNOUNCE.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/CHANGE.LOG
%doc %{_texmfdistdir}/doc/latex/nicetext/FILEs.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/README
%doc %{_texmfdistdir}/doc/latex/nicetext/README.pdf
%doc %{_texmfdistdir}/doc/latex/nicetext/RELEAS03.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/RELEAS04.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/RELEAS05.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/RELEASE042.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/RELEASE043.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/RELEASE044.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/RELEASE051.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/demo/arseneau.pdf
%doc %{_texmfdistdir}/doc/latex/nicetext/demo/iso.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/demo/lns.txt
%doc %{_texmfdistdir}/doc/latex/nicetext/demo/sample.tex
%doc %{_texmfdistdir}/doc/latex/nicetext/demo/substr.pdf
%doc %{_texmfdistdir}/doc/latex/nicetext/fifinddo.pdf
%doc %{_texmfdistdir}/doc/latex/nicetext/makedoc.pdf
%doc %{_texmfdistdir}/doc/latex/nicetext/mdoccheat.pdf
%doc %{_texmfdistdir}/doc/latex/nicetext/niceverb.pdf
%doc %{_texmfdistdir}/doc/latex/nicetext/wikicheat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nicetext/README.tex
%doc %{_texmfdistdir}/source/latex/nicetext/fifinddo.tex
%doc %{_texmfdistdir}/source/latex/nicetext/makedoc.tex
%doc %{_texmfdistdir}/source/latex/nicetext/mdoccheat.tex
%doc %{_texmfdistdir}/source/latex/nicetext/niceverb.tex
%doc %{_texmfdistdir}/source/latex/nicetext/srcfiles.tex
%doc %{_texmfdistdir}/source/latex/nicetext/wikicheat.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
