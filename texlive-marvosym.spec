# revision 29349
# category Package
# catalog-ctan /fonts/marvosym
# catalog-date 2012-04-08 13:55:52 +0200
# catalog-license ofl
# catalog-version 2.2a
Name:		texlive-marvosym
Version:	2.2a
Release:	12
Summary:	Martin Vogel's Symbols (marvosym) font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/marvosym
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Martin Vogel's Symbol font (marvosym) contains the Euro
currency symbol as defined by the European commission, along
with symbols for structural engineering; symbols for steel
cross-sections; astronomy signs (sun, moon, planets); the 12
signs of the zodiac; scissor symbols; CE sign and others. The
package contains both the original TrueType font and the
derived Type 1 font, together with support files for TeX
(LaTeX).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/marvosym/marvosym.afm
%{_texmfdistdir}/fonts/map/dvips/marvosym/marvosym.map
%{_texmfdistdir}/fonts/tfm/public/marvosym/umvs.tfm
%{_texmfdistdir}/fonts/truetype/public/marvosym/marvosym.ttf
%{_texmfdistdir}/fonts/type1/public/marvosym/marvosym.pfb
%{_texmfdistdir}/tex/latex/marvosym/marvosym.sty
%{_texmfdistdir}/tex/latex/marvosym/umvs.fd
%doc %{_texmfdistdir}/doc/fonts/marvosym/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/marvosym/Makefile
%doc %{_texmfdistdir}/doc/fonts/marvosym/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/marvosym/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/marvosym/README
%doc %{_texmfdistdir}/doc/fonts/marvosym/marvodoc.pdf
%doc %{_texmfdistdir}/doc/fonts/marvosym/marvodoc.tex
%doc %{_texmfdistdir}/doc/fonts/marvosym/marvosym-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/marvosym/marvosym-doc.tex
#- source
%doc %{_texmfdistdir}/source/fonts/marvosym/generate_marvosym_derivs.sh
%doc %{_texmfdistdir}/source/fonts/marvosym/patch_marvosym_afm.sed
%doc %{_texmfdistdir}/source/fonts/marvosym/patch_marvosym_pfb.sed

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
