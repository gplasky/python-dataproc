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
# Snippet for InstantiateWorkflowTemplate
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataproc


# [START dataproc_generated_dataproc_v1_WorkflowTemplateService_InstantiateWorkflowTemplate_sync]
from google.cloud import dataproc_v1


def sample_instantiate_workflow_template():
    # Create a client
    client = dataproc_v1.WorkflowTemplateServiceClient()

    # Initialize request argument(s)
    request = dataproc_v1.InstantiateWorkflowTemplateRequest(
        name="name_value",
    )

    # Make the request
    operation = client.instantiate_workflow_template(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END dataproc_generated_dataproc_v1_WorkflowTemplateService_InstantiateWorkflowTemplate_sync]
