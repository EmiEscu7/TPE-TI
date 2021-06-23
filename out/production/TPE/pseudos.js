RLC_coding(fuente){
    codigo = ""
    simb_act = fuente[0]
    cant_act_simb = 1
    i = 1

    while (i < fuente.size()){
        s = fuente[i]
        if(s == simb_act){
            cant_act_simb += 1
        } else {
            codigo = codigo + simb_act + cant_act_simb
            simb_act = s
            cant_act_simb = 1
        }            
        i += 1
    }    
      
    return codigo
}