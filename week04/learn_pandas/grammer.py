import warnings

if 5 in [1,2,3,4]:
    print('right')
else:
    warnings.warn("This is a wrong message",FutureWarning,
                stacklevel=2,)