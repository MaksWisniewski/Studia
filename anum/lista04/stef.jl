using Printf

function steffensen(f, c=0, iter=10)
    c = BigFloat(c)
    for i in 1:iter
        oldc = c
        fc = f(c)
        fcfc = f(c+fc)
        c -= (fc^2)/(fcfc-fc)

        if isnan(c) || isinf(c) 
            return oldc
        end
        @printf("iteracja %2d: c = %9.10f, eps = %9.4e\n", i, c, abs((c-oldc)/c))
    end
    c
end

f(x) = exp(-x)-sin(x)

setprecision(512)
println(steffensen(f,0))
