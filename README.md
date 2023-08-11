# aiml_model_wrapper

An OTP library

## Build

    $ rebar3 compile

## Run

### Using the wrapper

```sh
P = aiml_model_wrapper:init(<model_name>, <version>, <python binary>).
aiml_model_wrapper:evaluate(P, <features>).
```

The features should be provided in the below format.

```erlang
#{idc_time => 0.31546242796601565,x_goal => 4.797916775581953,
  x_start => 7.467803130327546,y_goal => 9.016381327933473,
  y_start => 1.4935645558846233}
```

An example of using the wrapper is provided in the sample module located in the `src/` directory.
