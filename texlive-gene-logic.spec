# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gene/logic
# catalog-date 2008-10-04 10:00:56 +0200
# catalog-license other-free
# catalog-version 1.4
Name:		texlive-gene-logic
Version:	1.4
Release:	1
Summary:	Typeset logic formulae, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/logic
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gene-logic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gene-logic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a facility to typeset certain logic
formulae. It provides an environment like eqnarray, an extended
newtheorem environment, and several macros.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gene-logic/gn-logic14.sty
%doc %{_texmfdistdir}/doc/latex/gene-logic/gn-logic14.pdf
%doc %{_texmfdistdir}/doc/latex/gene-logic/gn-logic14.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
