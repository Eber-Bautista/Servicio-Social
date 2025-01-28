# Actividades realizadas
En este README se encontrará un resumen de cada una de las actividades realizadas para el servicio social llamado _"Desarrollo de software libre para la manipulación de objetos cuánticos en notación de Dirac"_ a cargo del Dr. Pablo Barberis Blostein.
## 1. Librerías SciPy, Sympy (_Python_), y GSL (_C_)
La primera parte consistió en familiarizarse con las tres librerías principales para el desarrollo de ***OpenKet***. Dos son librerías de Python: SciPy y Sympy; la primera provee una amplia variedad de funciones empleadas en ciencia e ingeniería, la segunda permite resolver problemas matemáticos de manera simbólica. Por otro lado, GSL (_GNU Scientific Library_) es una librería en C que tiene una gran cantidad de rutinas matemáticas, funciones especiales, ajuste por mínimos cuadrados y demás.
La manera que se propuso para la familiarización de estas librerías fue usarlas para resolver la ecuación del Oscilador Amortiguado y Forzado:

$$m\frac{d^2x}{dt^2}=F_0\cos(\omega t)-b\frac{dx}{dt}-kx$$

Para resolver esta ecuación en SciPy y en GSL, fue necesario convertir la EDO de segundo orden anterior en un sistema de EDOs de primer orden.

$$\frac{dv}{dt}=\frac{F_0}{m}\cos(\omega t)-\frac{b}{m}v-\frac{k}{m}x$$
$$\frac{dx}{dt}=v$$

En el caso de SciPy, se utilizó la función `odeint` para resolver el sistema de EDOs con condiciones iniciales en la posición y velocidad. Por su parte, GSL usa un tipo de dato llamado `gsl_odeiv2_system` para definir el sistema de ecuaciones y para resolverlo se empleó el Driver `gsl_odeiv2_driver_alloc_y_new`.

Por otro lado, Sympy puede trabajar directamente con la ecuación original, lo único que se hizo fueron definir los símbolos y la función que se está derivando, usando `symbols` y `Function` respectivamente, para luego usar `dsolve`para resolver la ecuación. Entonce, la solución analítica obtenida con SymPy es

$$x{\left(t \right)} = C_{1} e^{\frac{t \left(- b + \sqrt{b^{2} - 4 k m}\right)}{2 m}} + C_{2} e^{- \frac{t \left(b + \sqrt{b^{2} - 4 k m}\right)}{2 m}} + \frac{F_{0} b \omega \sin{\left(\omega t \right)}}{b^{2} \omega^{2} + k^{2} - 2 k m \omega^{2} + m^{2} \omega^{4}} + \frac{F_{0} k \cos{\left(\omega t \right)}}{b^{2} \omega^{2} + k^{2} - 2 k m \omega^{2} + m^{2} \omega^{4}} - \frac{F_{0} m \omega^{2} \cos{\left(\omega t \right)}}{b^{2} \omega^{2} + k^{2} - 2 k m \omega^{2} + m^{2} \omega^{4}}$$

A continución se muestra la solución arrojada por cada librería para la ecuación del Oscilador Amortiguado y Forzado para parámetros $$F_0=2,\omega=6,b=0.3,k=2,m=1$$ y condiciones iniciales $$x_0=4,v_0=-5$$


![SolucionesOscilador](https://github.com/user-attachments/assets/e69f5e3f-ae0b-4278-b31b-d4b80fbb186e)
