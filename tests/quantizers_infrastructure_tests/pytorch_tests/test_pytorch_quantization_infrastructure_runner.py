# Copyright 2021 Sony Semiconductor Israel, Inc. All rights reserved.
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
# ==============================================================================


import unittest

from model_compression_toolkit import TrainingMethod
from model_compression_toolkit.core.common.target_platform import QuantizationMethod
from model_compression_toolkit.quantizers_infrastructure import QuantizationTarget, BasePyTorchInferableQuantizer, \
    BasePytorchTrainableQuantizer
from tests.quantizers_infrastructure_tests.pytorch_tests.test_pytorch_base_quantizer import \
    TestPytorchBaseWeightsQuantizer, TestPytorchBaseActivationQuantizer, TestPytorchQuantizerWithoutMarkDecorator
from tests.quantizers_infrastructure_tests.pytorch_tests.test_pytorch_get_quantizers import TestGetInferableQuantizer, \
    TestGetTrainableQuantizer
from tests.quantizers_infrastructure_tests.pytorch_tests.test_pytorch_quantization_wrapper import \
    TestPytorchWeightsQuantizationWrapper, TestPytorchActivationQuantizationWrapper


class PytorchInfrastructureTest(unittest.TestCase):

    def test_layer_pytorch_infrastructre(self):
        TestPytorchWeightsQuantizationWrapper(self).run_test()
        TestPytorchActivationQuantizationWrapper(self).run_test()


    def test_pytorch_base_quantizer(self):
        TestPytorchBaseWeightsQuantizer(self).run_test()
        TestPytorchBaseActivationQuantizer(self).run_test()
        TestPytorchQuantizerWithoutMarkDecorator(self).run_test()

    def test_pytorch_get_quantizers(self):
        TestGetInferableQuantizer(self, quant_target=QuantizationTarget.Weights,
                                  quant_method=QuantizationMethod.POWER_OF_TWO,
                                  quantizer_base_class=BasePyTorchInferableQuantizer)
        TestGetInferableQuantizer(self, quant_target=QuantizationTarget.Weights,
                                  quant_method=QuantizationMethod.SYMMETRIC,
                                  quantizer_base_class=BasePyTorchInferableQuantizer)
        TestGetInferableQuantizer(self, quant_target=QuantizationTarget.Weights,
                                  quant_method=QuantizationMethod.UNIFORM,
                                  quantizer_base_class=BasePyTorchInferableQuantizer)
        TestGetInferableQuantizer(self, quant_target=QuantizationTarget.Activation,
                                  quant_method=QuantizationMethod.POWER_OF_TWO,
                                  quantizer_base_class=BasePyTorchInferableQuantizer)
        TestGetInferableQuantizer(self, quant_target=QuantizationTarget.Activation,
                                  quant_method=QuantizationMethod.SYMMETRIC,
                                  quantizer_base_class=BasePyTorchInferableQuantizer)
        TestGetInferableQuantizer(self, quant_target=QuantizationTarget.Activation,
                                  quant_method=QuantizationMethod.UNIFORM,
                                  quantizer_base_class=BasePyTorchInferableQuantizer)

        TestGetTrainableQuantizer(self, quant_target=QuantizationTarget.Weights,
                                  quant_method=QuantizationMethod.POWER_OF_TWO,
                                  quantizer_base_class=BasePytorchTrainableQuantizer, quantizer_type=TrainingMethod.STE)
        TestGetTrainableQuantizer(self, quant_target=QuantizationTarget.Weights,
                                  quant_method=QuantizationMethod.SYMMETRIC,
                                  quantizer_base_class=BasePytorchTrainableQuantizer, quantizer_type=TrainingMethod.STE)
        TestGetTrainableQuantizer(self, quant_target=QuantizationTarget.Weights,
                                  quant_method=QuantizationMethod.UNIFORM,
                                  quantizer_base_class=BasePytorchTrainableQuantizer, quantizer_type=TrainingMethod.STE)
        TestGetTrainableQuantizer(self, quant_target=QuantizationTarget.Activation,
                                  quant_method=QuantizationMethod.POWER_OF_TWO,
                                  quantizer_base_class=BasePytorchTrainableQuantizer, quantizer_type=TrainingMethod.STE)
        TestGetTrainableQuantizer(self, quant_target=QuantizationTarget.Activation,
                                  quant_method=QuantizationMethod.SYMMETRIC,
                                  quantizer_base_class=BasePytorchTrainableQuantizer, quantizer_type=TrainingMethod.STE)
        TestGetTrainableQuantizer(self, quant_target=QuantizationTarget.Activation,
                                  quant_method=QuantizationMethod.UNIFORM,
                                  quantizer_base_class=BasePytorchTrainableQuantizer, quantizer_type=TrainingMethod.STE)


if __name__ == '__main__':
    unittest.main()