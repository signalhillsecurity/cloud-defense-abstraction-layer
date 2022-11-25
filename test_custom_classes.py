from ast import Try
from multiprocessing import Value
from random import sample
import pytest 
from CdalTechnique import Technique


@pytest.mark.parametrize('clouds',['AWS', 'AZURE', 'GCP', 'OCI'])



@pytest.fixture
def sample_technique():
    a = Technique("T000", "AWS")
    return a 


class TestTechniqueClass:
    @pytest.mark.parametrize('clouds',['AWS', 'AZURE', 'GCP', 'OCI'])
    def test_change_cloud_upper_good(sample_technique, clouds):
        sample_technique.cloud= clouds
        assert sample_technique.cloud == clouds

    def test_change_cloud_lower_good(sample_technique):
        sample_technique.cloud = "azure"
        assert sample_technique.cloud == "AZURE"

    def test_change_cloud_bad(sample_technique):
        try:
            sample_technique.cloud = "not a cloud"
            assert False
        except ValueError:
            assert True
    
