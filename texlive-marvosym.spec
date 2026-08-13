%global tl_name marvosym
%global tl_revision 79618
%global tl_version 2.2a

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Martin Vogel's Symbol font (marvosym) contains the Euro currency symbol
as defined by the European commission, along with symbols for structural
engineering; symbols for steel cross-sections; astronomy signs (sun,
moon, planets); the 12 signs of the zodiac; scissor symbols; CE sign and
others. The package contains both the original TrueType font and the
derived Type 1 font, together with support files for TeX (LaTeX).


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from marvosym:
Map marvosym.map
TL_DROPIN_EOF
