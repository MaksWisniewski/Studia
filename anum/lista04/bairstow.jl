using OffsetArrays
using Printf
using Polynomials
BF = BigFloat
setprecision(128)

function emptyArray(type, size)
    return OffsetVector{type}(undef, 0:(size - 1))
end

function bairstow(n, p, u, v, iterations)
    b = emptyArray(BF, n + 1)
    c = emptyArray(BF, n + 1)
    b[n] = p[n]
    c[n] = 0
    c[n - 1] = p[n]
    for j in 1:iterations
        b[n - 1] = p[n - 1] + u * b[n]
        for k in range(n - 2, 0, step=-1)
            b[k] = p[k] + u * b[k + 1] + v * b[k + 2]
            c[k] = b[k + 1] + u * c[k + 1] + v * c[k + 2]
        end
        J = c[0] * c[2] - c[1] * c[1]
        u += (c[1] * b[1] - c[2] * b[0]) / J
        v += (c[1] * b[0] - c[0] * b[1]) / J
    end
    return (u, v, b)
end

function evalPolynomial(p, x)
    res = BF(0)
    for i in range(size(p)[1] - 1, 0, step=-1)
        res = p[i] + res * x        
    end
    return res
end

function solveQuadratic(p)
    if p[1] != 0
        delta = p[2]^2 - 4p[1]p[3]
        delta += (delta < 0) ? 0im : 0
        if p[2] >= 0
            b = -p[2] - delta^0.5
            return (b / (2p[1]), 2p[3] / b)  # <=> P[3]/P[1] = b / (2P[1]) * X <=> X = 2P[3] / b
        else
            b = -p[2] + delta^0.5
            return [2p[3] / b, b / (2p[1])]
        end        
    elseif p[2] != 0
        return [-p[3] / p[2]]
    else
        return []
    end
end

function findRoots(p, u, v, iterations)
    u, v, b = bairstow(4, p, u, v, iterations)
    z1, z2 = solveQuadratic([1, -u, -v])
    z3, z4 = solveQuadratic([b[4], b[3], b[2]])
    return [z1, z2, z3, z4]
end

w = emptyArray(BF, 5)
w[0] = 1
w[1] = 2
w[2] = 3
w[3] = 4
w[4] = 5

u0 = BF(0.1)
v0 = BF(0.1)

roots_of_w = findRoots(w, u0, v0, 20)

for z in roots_of_w
    # println(evalPolynomial(w, z))
    res = evalPolynomial(w, z)
    @printf("Evaluation at root %.16f + %.16fi: %.16f + %.16fi\n", real(z), imag(z), real(res), imag(res))
end

roots_of_w2 = roots(Polynomial([1, 2, 3, 4, 5]))

function relError(x, y)
    return abs((x - y) / x)
end

for (z1, z2) in zip(roots_of_w, roots_of_w2)
    error = relError(z1, z2)
    @printf("Błąd względny między %.16f + %.16fi oraz %.16f + %.16fi: %.16f\n",
        real(z1), imag(z1), real(z2), imag(z2), error)
end