#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _ar_reg();
extern void _cad_reg();
extern void _cal_reg();
extern void _cat_reg();
extern void _k2_reg();
extern void _ka_reg();
extern void _kahp_reg();
extern void _kc_reg();
extern void _kdr_reg();
extern void _km2_reg();
extern void _naf_reg();
extern void _nap_reg();

modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," ar.mod");
fprintf(stderr," cad.mod");
fprintf(stderr," cal.mod");
fprintf(stderr," cat.mod");
fprintf(stderr," k2.mod");
fprintf(stderr," ka.mod");
fprintf(stderr," kahp.mod");
fprintf(stderr," kc.mod");
fprintf(stderr," kdr.mod");
fprintf(stderr," km2.mod");
fprintf(stderr," naf.mod");
fprintf(stderr," nap.mod");
fprintf(stderr, "\n");
    }
_ar_reg();
_cad_reg();
_cal_reg();
_cat_reg();
_k2_reg();
_ka_reg();
_kahp_reg();
_kc_reg();
_kdr_reg();
_km2_reg();
_naf_reg();
_nap_reg();
}
