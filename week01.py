# combinators
id = lambda x: x
k  = lambda x: lambda y: x

def repeated(f, n, x):
    if n == 0:
        return x
    else:
        return f(repeated(n - 1, f, x))
# repeated(3, lambda x:(x + 1), 5)

def c(n):
    return lambda f, lambda x: repeated(x, f, x)
# c(0)(2)(3)
# c(1)(lambda x:(x + 1))(3)


# consts
c0 = c(0)
c1 = c(1)

c_true = k
c_false = lambda x: id


cs = lambda n: lambda f: lambda x: f(n(f)(x
# cs(c(2))

def to_int(cn):
    return cn(lambda x:(x + 1))(0)
    
c_plus = lambda m:lambda n:lambda f: lambda x: m(f)(n(f)(x))

c_plus_prim = lambda m: m(cs)
# to_int(c_plus_prim(c(312))(c(324)))

c_mult = lambda m: lambda n: lambda f: m(n(f))

c_mult_prim = lambda m: lambda n: m(c_plus(n))(c0)

c_exp = lambda m: lambda n: n(m)

c_exp_prim = lambda m: lambda n: n(c_mult(m))(c1)

# to_int(c(7)(c(2)))

c_if = id
c_not = lambda b: lambda x: lambda y: b(y)(x)
c_and = lambda b: lambda c: b(c)(b)
c_or = lambda b: lambda c: b(b)(c)

def to_bool(cb):
    return cb(True)(False)
# to_bool(c_not(c_true))

c_is_zero = lambda n: n(k(c_false))(c_true)

c_is_even = lambda n: (c_not)(c_true)
c_is_odd = lambda n: (c_not)(c_false)

c_pair = lambda x: lambda y: lambda z: z(x)(y)
c_left = lambda p: p(c_true)
c_right = lambda p: p(c_false)

def to_int_pair(cp):
#    return (to_int(c_left(cp)), to_int(c_right(cp)))
    return cp(lambda x: lambda y: (to_int(x), to_int(y)))

cp = lambda n: c_right(n(lambda p: c_pair(cs(c_left(p)))(c_left(p)))(c_pair(c0)(c0)))

c_base_fact = c_pair(c0)(c1)
c_step_fact = lambda p: c_pair(cs(c_left(p)))(c_mult(cs(c_left(p)))(c_right(p)))
c_fact = lambda n: c_right(n(c_step_fact)(c_base_fact))

# fixed point function
Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))
Z = lambda f: (lambda x: f(lambda z: x(x)(z)))(lambda x: f(lambda z: x(x)(z)))

omega = lambda x: x(x)

gamma_fact = lambda f: lambda n: c_is_zero(n)(c1)(c_mult(n)(f(cp(n))))
gamma_fact_Z = lambda f: lambda n: c_is_zero(n)(lambda z: c1(z))(lambda z: c_mult(n)(f(cp(n)))(z))


c_fact_fact = Y(gamma_fact)
c_fact_fact_Z = Z(gamma_fact)
