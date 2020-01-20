SUBROUTINE evalute_ishigami_f2py(rslt, inputs, num_evals)

    INTEGER, INTENT(IN) :: num_evals

    DOUBLE PRECISION, INTENT(OUT)   :: rslt(num_evals)

    DOUBLE PRECISION, INTENT(IN)    :: inputs(:, :)

    DOUBLE PRECISION :: a, b


    INTEGER :: i

    DOUBLE PRECISION :: x(3)

    a = 7.0
    b = 0.1

    DO i = 1, num_evals
      x = inputs(i, :)
      rslt(i) = SIN(x(1)) + a * SIN(x(2)) ** 2 + b * x(3) ** 4 * SIN(x(1))
    END DO

END SUBROUTINE
