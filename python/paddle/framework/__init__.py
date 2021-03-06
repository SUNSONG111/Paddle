#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TODO: import framework api under this directory 
__all__ = [
    'create_global_var', 'create_parameter', 'ParamAttr', 'Variable',
    'CPUPlace', 'CUDAPlace', 'CUDAPinnedPlace'
]

__all__ += [
    'BackwardStrategy', 'grad', 'LayerList', 'load', 'save', 'prepare_context',
    'to_variable', 'no_grad', 'ParallelEnv', 'DataParallel'
]

__all__ += [
    'NoamDecay', 'PiecewiseDecay', 'NaturalExpDecay', 'ExponentialDecay',
    'InverseTimeDecay', 'PolynomialDecay', 'CosineDecay'
]

from . import random
from .random import manual_seed

from ..fluid.framework import Variable  #DEFINE_ALIAS
from ..fluid.param_attr import ParamAttr  #DEFINE_ALIAS
from ..fluid.layers.tensor import create_global_var  #DEFINE_ALIAS
from ..fluid.layers.tensor import create_parameter  #DEFINE_ALIAS
from ..fluid.core import CPUPlace  #DEFINE_ALIAS
from ..fluid.core import CUDAPlace  #DEFINE_ALIAS
from ..fluid.core import CUDAPinnedPlace  #DEFINE_ALIAS

from paddle.fluid import core  #DEFINE_ALIAS
from ..fluid.dygraph.base import no_grad  #DEFINE_ALIAS
from ..fluid.dygraph.base import to_variable  #DEFINE_ALIAS
from ..fluid.dygraph.base import grad  #DEFINE_ALIAS
from ..fluid.dygraph.checkpoint import load_dygraph as load  #DEFINE_ALIAS
from ..fluid.dygraph.checkpoint import save_dygraph as save  #DEFINE_ALIAS
from ..fluid.dygraph.parallel import prepare_context  #DEFINE_ALIAS
from ..fluid.dygraph.parallel import ParallelEnv  #DEFINE_ALIAS
from ..fluid.dygraph.parallel import DataParallel  #DEFINE_ALIAS

from ..fluid.dygraph.learning_rate_scheduler import NoamDecay  #DEFINE_ALIAS
from ..fluid.dygraph.learning_rate_scheduler import PiecewiseDecay  #DEFINE_ALIAS
from ..fluid.dygraph.learning_rate_scheduler import NaturalExpDecay  #DEFINE_ALIAS
from ..fluid.dygraph.learning_rate_scheduler import ExponentialDecay  #DEFINE_ALIAS
from ..fluid.dygraph.learning_rate_scheduler import InverseTimeDecay  #DEFINE_ALIAS
from ..fluid.dygraph.learning_rate_scheduler import PolynomialDecay  #DEFINE_ALIAS
from ..fluid.dygraph.learning_rate_scheduler import CosineDecay  #DEFINE_ALIAS

BackwardStrategy = core.BackwardStrategy
