-module(aiml_model_wrapper).
-export([init/2, init/3, get_required_features/1, evaluate/2, stop/1]).

init(ModelName, Version, PythonLocation) ->
  PythonCodePath = code:priv_dir(aiml_model_wrapper),
  {ok, P} = python:start_link([{python_path, PythonCodePath}, {python, PythonLocation}]),
  python:call(P, program, init, [list_to_binary(ModelName), list_to_binary(Version)]),
  P.

init(ModelName, Version) ->
  init(ModelName, Version, "python3").

get_required_features(P) ->
  python:call(P, program, get_required_features, []).

evaluate(P, Features) ->
  SerializedFeatures = jiffy:encode(Features),
  python:call(P, program, evaluate, [SerializedFeatures]).

stop(P) ->
  python:stop(P).
