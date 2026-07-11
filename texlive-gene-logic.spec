%global tl_name gene-logic
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Typeset logic formulae, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gene/logic
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gene-logic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gene-logic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a facility to typeset certain logic formulae. It
provides an environment like eqnarray, a newtheorem-like environment
(NewTheorem), and several macros.

