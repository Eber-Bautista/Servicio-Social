from numpy import conjugate

def PureConcurrence(state):
    state=Normalize(state)
    rho=state*Adj(state)
    rho_A=TraceOut(rho,'B')
    return ((2*(round(1-Trace(rho_A*rho_A),10))))**0.5
    
def MixConcurrence(rho):
    Basis=[Ket(0,'A')*Ket(0,'B'),Ket(1,'A')*Ket(0,'B'),Ket(0,'A')*Ket(1,'B'),Ket(1,'A')*Ket(1,'B')]
    My=Qmatrix(Y('A')*Y('B'),Basis)
    Mrho=Qmatrix(rho,Basis)
    Mrho_=Matrix(conjugate(Mrho))
    R=Mrho*My*Mrho_*My
    L=R.eigenvals()
    L_lista=[]
    for l in L:
        for i in range(L[l]):
            L_lista.append((round(float(l),10)**2)**0.25)
    L_lista.sort(reverse=True)
    C=max(0,L_lista[0]-L_lista[1]-L_lista[2]-L_lista[3])
    return C

