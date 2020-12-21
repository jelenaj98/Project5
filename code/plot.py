import numpy as np
import matplotlib.pyplot as plt

a = False
b = False
c_ODE = False
c_MonteCarlo = False
d_ODE = False
d_MonteCarlo = False
e_ODE = False
e_MonteCarlo = False


if a:
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Population A")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Population B")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Population C")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Population D")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

if b:
    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Monte Carlo, Population A")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Monte Carlo, Population B")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, Mc", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Monte Carlo, Population C")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, Mc", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Monte Carlo, Population D")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

if c_ODE:
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vital_dynamics_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Vital dynamics with Runge-Kutta, Population A")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vital_dynamics_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Vital dynamics with Runge-Kutta, Population B")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vital_dynamics_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Vital dynamics with Runge-Kutta, Population C")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vital_dynamics_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Vital dynamics with Runge-Kutta, Population D")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

if c_MonteCarlo:
    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_vital_dynamics_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, Mc", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vital_dynamics_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Vital dynamics with Runge-Kutta, Population A")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_vital_dynamics_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, Mc", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vital_dynamics_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Vital dynamics, Population B")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_vital_dynamics_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vital_dynamics_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Vital dynamics, Population C")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_vital_dynamics_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vital_dynamics_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Vital dynamics, Population D")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

if d_ODE:
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_seasonal_variation_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Sesonal Variation, Population A")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_seasonal_variation_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Sesonal Variation, Population B")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_seasonal_variation_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Sesonal Variation, Population C")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_seasonal_variation_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Sesonal Variation, Population D")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

if d_MonteCarlo:
    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_seasonal_variation_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_seasonal_variation_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Seasonal Variation, Population A")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_seasonal_variation_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_seasonal_variation_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Seasonal Variation, Population B")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_seasonal_variation_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_seasonal_variation_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Seasonal Variation, Population C")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_seasonal_variation_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_seasonal_variation_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Seasonal Variation, Population D")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

if e_ODE:
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vaccination_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Vaccination, Population A")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vaccination_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Vaccination, Population B")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vaccination_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Vaccination, Population C")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vaccination_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S", color='#F5B14C')
    plt.plot(tid,I, label ="I", color="forestgreen")
    plt.plot(tid,R, label="R", color="salmon")
    plt.title("Runga Kutta, Vaccination, Population D")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

if e_MonteCarlo:
    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_vaccination_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vaccination_A.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Vaccination, Population A")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_vaccination_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vaccination_B.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Vaccination, Population B")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_vaccination_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vaccination_C.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Vaccination, Population C")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()

    tid, S, I, R = np.loadtxt("../outputs/monteCarlo_vaccination_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, MC", color='#F5B14C')
    plt.plot(tid,I, label ="I, MC", color="forestgreen")
    plt.plot(tid,R, label="R, MC", color="salmon")
    tid, S, I, R = np.loadtxt("../outputs/rungeKutta_vaccination_D.txt", usecols=(0,1,2,3), unpack =True)
    plt.plot(tid,S, label="S, RK4", color='tab:orange')
    plt.plot(tid,I, label ="I, RK4", color="tab:green")
    plt.plot(tid,R, label="R, RK4", color="tab:red")
    plt.title("Vaccination, Population D")
    plt.ylabel("Number of people")
    plt.xlabel("Time [days]")
    plt.legend()
    plt.show()
