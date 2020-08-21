"""Constants which are used as dataset properties.
"""
BINARY_CLASSIFICATION = 1
MULTICLASS_CLASSIFICATION = 2
MULTILABEL_CLASSIFICATION = 3
REGRESSION = 4
MULTIOUTPUT_REGRESSION = 5

REGRESSION_TASKS = [REGRESSION, MULTIOUTPUT_REGRESSION]
CLASSIFICATION_TASKS = [BINARY_CLASSIFICATION, MULTICLASS_CLASSIFICATION,
                        MULTILABEL_CLASSIFICATION]

TASK_TYPES = REGRESSION_TASKS + CLASSIFICATION_TASKS

TASK_TYPES_TO_STRING = \
    {BINARY_CLASSIFICATION: "binary.classification",
     MULTICLASS_CLASSIFICATION: "multiclass.classification",
     MULTILABEL_CLASSIFICATION: "multilabel.classification",
     REGRESSION: "regression",
     MULTIOUTPUT_REGRESSION: "multioutput.regression"}

STRING_TO_TASK_TYPES = \
    {"binary.classification": BINARY_CLASSIFICATION,
     "multiclass.classification": MULTICLASS_CLASSIFICATION,
     "multilabel.classification": MULTILABEL_CLASSIFICATION,
     "regression": REGRESSION,
     "multioutput.regression": MULTIOUTPUT_REGRESSION}

DENSE = 6
SPARSE = 7
PREDICTIONS = 8
INPUT = 9

SIGNED_DATA = 10
UNSIGNED_DATA = 11

DATASET_PROPERTIES_TO_STRING = \
    {DENSE:         'dense',
     SPARSE:        'sparse',
     PREDICTIONS:   'predictions',
     INPUT:         'input',
     SIGNED_DATA:   'signed data',
     UNSIGNED_DATA: 'unsigned data'}