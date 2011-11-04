# revision 23630
# category Package
# catalog-ctan /fonts/marvosym
# catalog-date 2011-08-21 12:30:47 +0200
# catalog-license ofl
# catalog-version 2.2
Name:		texlive-marvosym
Version:	2.2
Release:	1
Summary:	Martin Vogel's Symbols (marvosym) font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/marvosym
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marvosym.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Martin Vogel's Symbol (marvosym) font contains the Euro
currency symbol as defined by the European commission, and also
in shapes to blend with typefaces Times, Helvetica and Courier;
symbols for structural engineering; symbols for steel cross-
sections; astronomy signs (sun, moon, planets); the 12 signs of
the zodiac; scissor symbols; CE sign and others. The package
contains both original TrueType font as well as derived Type 1
and support files for TeX (LaTeX).

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
%{_texmfdistdir}/fonts/afm/public/marvosym/marvosym.afm
%{_texmfdistdir}/fonts/map/dvips/marvosym/marvosym.map
%{_texmfdistdir}/fonts/tfm/public/marvosym/umvs.tfm
%{_texmfdistdir}/fonts/truetype/public/marvosym/marvosym.ttf
%{_texmfdistdir}/fonts/type1/public/marvosym/marvosym.pfb
%{_texmfdistdir}/tex/latex/marvosym/marvosym.sty
%{_texmfdistdir}/tex/latex/marvosym/umvs.fd
%doc %{_texmfdistdir}/doc/fonts/marvosym/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/marvosym/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/marvosym/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/marvosym/README
%doc %{_texmfdistdir}/doc/fonts/marvosym/marvodoc.pdf
%doc %{_texmfdistdir}/doc/fonts/marvosym/marvodoc.tex
#- source
%doc %{_texmfdistdir}/source/fonts/marvosym/generate_marvosym_derivs.sh
%doc %{_texmfdistdir}/source/fonts/marvosym/patch_marvosym_afm.sed
%doc %{_texmfdistdir}/source/fonts/marvosym/patch_marvosym_pfb.sed
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}