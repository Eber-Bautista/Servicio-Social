from numpy import conjugate

def PureConcurrence(state,htag):
    """
    This function calculates the concurrence of a pure state of a bipartite system
    :param state: Total expression of vector(s) or a bipartite quantum state  
    :type state: :obj:`openket.DiracObject`
    :param htag: Tag of any of the two Hilbert spaces of the bipartite system
    :type htag: string
    :return: Concurrence of the pure state
    :rtype: float
    """
    state=Normalize(state)
    rho=state*Adj(state)
    rho_A=TraceOut(rho,htag)
    return ((2*(round(1-Trace(rho_A*rho_A),10))))**0.5
    
def MixConcurrence(rho,htag1,htag2):
    """
    This function calculates the concurrence of a mixed state of a bipartite system
    :param rho: Bipartite density operator   
    :type state: Linear combination of :obj:`Ket`:obj:`Bra` objects
    :param htag1: Tag of the first Hilbert space of the bipartite system
    :type htag1: string
    :param htag2: Tag of the second Hilbert space of the bipartite system
    :type htag2: string
    :return: Concurrence of the the mixed state
    :rtype: float
    """
    Basis=[Ket(i,htag1)*Ket(j,htag2) for i in range(2) for j in range(2)]
    My=Qmatrix(Y(htag1)*Y(htag2),Basis)
    Mrho=Qmatrix(rho,Basis)
    Mrho_=Matrix(conjugate(Mrho))
    R=Mrho*My*Mrho_*My
    L=R.eigenvals()
    L_list=[]
    for l in L:
        for i in range(L[l]):
            L_list.append((round(float(l),10)**2)**0.25)
    L_list.sort(reverse=True)
    C=max(0,L_list[0]-L_list[1]-L_list[2]-L_list[3])
    return C


