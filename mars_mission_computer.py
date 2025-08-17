import random

class DummySensor:
    def __init__(self):
        # 환경 값을 저장할 사전
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }

    def set_env(self):
        # 항목별로 지정된 범위의 랜덤 값 생성
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 1)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 1)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 1)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 1)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 3)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        # 환경 값 반환
        return self.env_values


# 실행 부분
if __name__ == '__main__':
    ds = DummySensor()        # 인스턴스 생성
    ds.set_env()              # 환경 값 설정
    values = ds.get_env()     # 환경 값 가져오기

    print('=== Dummy Sensor Environment ===')
    for key, value in values.items():
        print(f'{key}: {value}')