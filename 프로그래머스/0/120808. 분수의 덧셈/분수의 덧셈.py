import math 
def solution(numer1, denom1, numer2, denom2):
    denom = math.lcm(denom1, denom2) # 최소공배수 
    
    numer = denom // denom1 * numer1 + denom // denom2 * numer2
    
    gcd = math.gcd(numer, denom) # 최대공약수 
    
    return [numer // gcd, denom // gcd]