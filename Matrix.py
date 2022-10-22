'''This program is written by Kolawole Andrew to solve simulataneous equations using cramers rule,this module is intended to be incoporated 
into other projects since it comprises methods that require arguments and this arguments can include user inputs as well'''

                    
        
def solve_by2(a,b,c,d,e,f,det=False):
    
    (D0 )= (float(a)*float(e)) - (float(b)*float(d))
    (Dx )= (float(c)*float(e)) - (float(b)*float(f)) 
    (Dy )= (float(a)*float(f)) - (float(c)*float(d))
    
    try:
        X = float(Dx)/float(D0)
        Y = float(Dy/D0)
        return f"X = {round(X,2)},Y = {round(Y,2)}"
    except Exception as e:
        return str(e)
        
   

def by3Determinant(a,b,c,d,e,f,g,h,i):
    try:
        det = float(a*((e*i)-(h*f))) +(-b*((d*i)-(f*g)) )+ (c*((d* h)-(e*g)))
        return det
    except:
        return  'Error'
        

def solve_by3(eqn1,eqn2,eqn3):

    a , b ,c , d = float(eqn1.split(',')[0]),float(eqn1.split(',')[1]),float(eqn1.split(',')[2]),float(eqn1.split(',')[3])
    e, f, g, h = float(eqn2.split(',')[0]),float(eqn2.split(',')[1]),float(eqn2.split(',')[2]),float(eqn2.split(',')[3])
    i, j, k , l = float(eqn3.split(',')[0]),float(eqn3.split(',')[1]),float(eqn3.split(',')[2]),float(eqn3.split(',')[3])
    
    
    try:
        det_0 = by3Determinant(a ,b,c ,e,f,g,i,j,k)
        det_1 = by3Determinant(d,b,c,h,f,g,l,j,k)
        det_2 = by3Determinant(a,d,c,e,h,g,i,l,k)
        det_3 = by3Determinant(a,b,d,e,f,h,i,j,l)
        x ,y,z= (det_1/det_0),(det_2/det_0),(det_3/det_0)
        return f"X: {round(x,2)} Y: {round(y,2)} Z: {round(z,2)}"
    except:
        return  'Error'

def quadratic(a,b,c):
    try:
        discriminant = float((((float(b)**2))-(4*(float(a)*float(c))))**(0.5))
        to_add = (float(b)*-1)
        denum = (float(a)*2)
        root_1 = float((to_add+discriminant)/(denum))
        root_2 = float((to_add-discriminant)/(denum))
    except:
        return 'Error'
    
    return f"X: {round(root_1,2)} or X: {round(root_2,2)}"
    
        
