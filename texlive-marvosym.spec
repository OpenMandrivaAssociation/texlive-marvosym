%global tl_name marvosym
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2a
Release:	%{tl_revision}.1
Summary:	Martin Vogels Symbols (marvosym) font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/marvosym
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Martin Vogel's Symbol font (marvosym) contains the Euro currency symbol
as defined by the European commission, along with symbols for structural
engineering; symbols for steel cross-sections; astronomy signs (sun,
moon, planets); the 12 signs of the zodiac; scissor symbols; CE sign and
others. The package contains both the original TrueType font and the
derived Type 1 font, together with support files for TeX (LaTeX).

