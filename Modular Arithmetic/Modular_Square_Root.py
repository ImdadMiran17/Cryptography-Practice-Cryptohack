# Using Sage Math

from sage.rings.finite_rings.integer_mod import square_root_mod_prime

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

print(square_root_mod_prime(Mod(a, p), p))



# Solution 1

def legendre(a,p):
	return pow(a, (p-1)//2, p)

def tonelli(a,p):
	assert legendre(a,p) == 1, "not a square (mod p)"
	q = p - 1
	s = 0 
	while q%2 == 0:
		q//=2
		s += 1
	if s == 1:
		return pow(a, (p+1)//4, p)
	for z in range(2,p):  #quadratic non-residue(z)
		if p-1 == legendre(z,p):
			break

	c = pow(z, q, p)  # c <- z^q
	r = pow(a, (q+1)//2, p) #r <- n^q
	t = pow(a, q, p)  # t <- n^q
	m = s # m <-s
	t2 = 0 
	while (t-1)%p != 0:  #t=0 or t=1
		t2 = (t*t)%p 
		for i in range(1, m): #0<i<m t^2*i = 1
			if (t2-1)%p == 0:
				break
			t2 = (t2 * t2)%p 
		b = pow(c, 1 << (m - i - 1),p) #b <- c^2m-i-1
		r = (r*b)%p #r <-rb
		c = (b*b)%p #c <-b^2
		t = (t*c)%p #t <-t*b^2
		m = i  #m <- i
	return r


if __name__ == '__main__':
	ttest = [(a,p)]
	for a,p in ttest:
		r = tonelli(a,p)
		assert (r*r-a)%p == 0
		print(f"\t roots : {r}, {p-r}")

		#r is first solution, second solution is -r, mod p == p-r



# Solution 2

def legendre_symbol(a, p):
    """
    Legendre symbol
    Define if a is a quadratic residue modulo odd prime
    http://en.wikipedia.org/wiki/Legendre_symbol
    """
    ls = pow(a, (p - 1)/2, p)
    if ls == p - 1:
        return -1
    return ls

def prime_mod_sqrt(a, p):
    """
    Square root modulo prime number
    Solve the equation
        x^2 = a mod p
    and return list of x solution
    http://en.wikipedia.org/wiki/Tonelli-Shanks_algorithm
    """
    a %= p

    # Simple case
    if a == 0:
        return [0]
    if p == 2:
        return [a]

    # Check solution existence on odd prime
    if legendre_symbol(a, p) != 1:
        return []

    # Simple case
    if p % 4 == 3:
        x = pow(a, (p + 1)/4, p)
        return [x, p-x]

    # Factor p-1 on the form q * 2^s (with Q odd)
    q, s = p - 1, 0
    while q % 2 == 0:
        s += 1
        q //= 2

    # Select a z which is a quadratic non resudue modulo p
    z = 1
    while legendre_symbol(z, p) != -1:
        z += 1
    c = pow(z, q, p)

    # Search for a solution
    x = pow(a, (q + 1)/2, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        # Find the lowest i such that t^(2^i) = 1
        i, e = 0, 2
        for i in xrange(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2

        # Update next value to iterate
        b = pow(c, 2**(m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    return [x, p-x]

print(min(prime_mod_sqrt(a,p)))


