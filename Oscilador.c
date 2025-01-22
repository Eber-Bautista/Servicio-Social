#include <stdio.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_odeiv2.h>
typedef struct{   //Se define una estructura que contenga los parámetros involucrados en la ecuación diferencial del oscilador
  double F0;
  double omega;
  double b;
  double k;
  double m;
}Parametros;

Parametros params={2.0,6.0,0.3,2.0,1.0}; // Se eligieron los mismos valores usados para SciPy y SymPy 
int
func (double t, const double y[], double f[],
      void *params) //Se define el sistema de ecuaciones a resolver (pues se pasó de una única EDO de segundo orden a un sistema de dos EDOs de primer orden)
{
  Parametros *p=(Parametros *)params; //Se cambia el puntero params para pasar del tipo (void *) al tipo (Parametros *)
  double F0=p->F0;
  double omega=p->omega;
  double b=p->b;
  double k=p->k;
  double m=p->m;
  f[0] = y[1];
  f[1] = (F0*cos(omega*t)-b*y[1]-k*y[0])/m;
  return GSL_SUCCESS;
}

int
main (void)
{
  gsl_odeiv2_system sys = {func, NULL, 2, &params};//Se crea la estructura del tipo gsl_odeiv2_system., esta es una estructura utilizada en GSL para definir el sistema de EDOs a resolver. El NULL aparece dado que no es necesario incluir el jacobiano en este caso

  gsl_odeiv2_driver * d =
    gsl_odeiv2_driver_alloc_y_new (&sys, gsl_odeiv2_step_rk8pd,
                                  1e-6, 1e-6, 0.0); //Se crea un driver que resuelva el sistema de ecuaciones 
  int i;
  double t = 0.0, t1 = 20.0;
  double y[2] = { 4.0, -5.0 }; //condiciones iniciales en x y v

  for (i = 1; i <= 100; i++)
    {
      double ti = i * t1 / 100.0;
      int status = gsl_odeiv2_driver_apply (d, &t, ti, y);

      if (status != GSL_SUCCESS)
        {
          printf ("error, return value=%d\n", status);
          break;
        }

      FILE *file=fopen("SolucionOscilador.dat","a"); //Se guarda la solución en un archivo tipo dat
      if (file){
        fprintf(file,"%.5e\t%.5e\t%.5e\n",t,y[0],y[1]);
        fclose(file);
      } else{
      printf("Error");
      }
    }

  gsl_odeiv2_driver_free (d);
  return 0;
}
