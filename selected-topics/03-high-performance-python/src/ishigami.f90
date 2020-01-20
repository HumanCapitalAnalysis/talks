SUBROUTINE evalute_ishigami_f2py(rslt, inputs, num_evals)
  !
  ! Minimal exaple for interfacing FORTRAN and PYHON using the evaluation of
  ! the Ishigami function as a use case.
  !
  !-----------------------------------------------------------------------------
  ! Dummy variables
  !-----------------------------------------------------------------------------

  DOUBLE PRECISION, INTENT(OUT)   :: rslt(num_evals)

  DOUBLE PRECISION, INTENT(IN)    :: inputs(:, :)

  INTEGER, INTENT(IN)             :: num_evals

  !-----------------------------------------------------------------------------
  ! Local variables
  !-----------------------------------------------------------------------------

  INTEGER          :: i

  DOUBLE PRECISION :: x(3)

  !-----------------------------------------------------------------------------
  ! Algorithm
  !-----------------------------------------------------------------------------

  DO i = 1, num_evals

    x = inputs(i, :)
    rslt(i) = SIN(x(1)) + 7.0 * SIN(x(2)) ** 2 + 0.1 * x(3) ** 4 * SIN(x(1))

  END DO

END SUBROUTINE
!*******************************************************************************
!*******************************************************************************
