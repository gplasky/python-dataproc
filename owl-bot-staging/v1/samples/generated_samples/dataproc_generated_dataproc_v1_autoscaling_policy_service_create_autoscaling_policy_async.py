# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateAutoscalingPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataproc


# [START dataproc_generated_dataproc_v1_AutoscalingPolicyService_CreateAutoscalingPolicy_async]
from google.cloud import dataproc_v1


async def sample_create_autoscaling_policy():
    # Create a client
    client = dataproc_v1.AutoscalingPolicyServiceAsyncClient()

    # Initialize request argument(s)
    policy = dataproc_v1.AutoscalingPolicy()
    policy.basic_algorithm.yarn_config.scale_up_factor = 0.1578
    policy.basic_algorithm.yarn_config.scale_down_factor = 0.1789
    policy.worker_config.max_instances = 1389

    request = dataproc_v1.CreateAutoscalingPolicyRequest(
        parent="parent_value",
        policy=policy,
    )

    # Make the request
    response = await client.create_autoscaling_policy(request=request)

    # Handle response
    print(response)

# [END dataproc_generated_dataproc_v1_AutoscalingPolicyService_CreateAutoscalingPolicy_async]