class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories


    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance} км; '
                f'Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        CALORIES_MEAN_SPEED_MULTIPLIER: int = 18
        CALORIES_MEAN_SPEED_SHIFT: float = 1.79
        HOURS_TO_MINUTES: int = 60
        return ((CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                 + CALORIES_MEAN_SPEED_SHIFT) * self.weight / self.M_IN_KM
                * (self.duration * HOURS_TO_MINUTES))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    LEN_STEP: float = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height


def get_spent_calories(self) -> float:
    KMH_TO_MS: float = 1000 / 3600
    HOURS_TO_MINUTES: int = 60
    MTRS_TO_CM: int = 100
    CALORIES_MEAN_SPEED_MULTIPLIER: float = 0.035
    CALORIES_MEAN_SPEED_SHIFT: float = 0.029
    return ((CALORIES_MEAN_SPEED_MULTIPLIER * self.weight
             + ((self.get_mean_speed() * KMH_TO_MS) ** 2
                // (self.height / MTRS_TO_CM))
             * CALORIES_MEAN_SPEED_SHIFT * self.weight)
            * (self.duration * HOURS_TO_MINUTES))


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool


    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool / self.M_IN_KM /
                self.duration)


    def get_spent_calories(self) -> float:
        CALORIES_MEAN_SPEED_SHIFT = 1.1
        return ((self.get_mean_speed() + CALORIES_MEAN_SPEED_SHIFT) * 2 *
                self.weight * self.duration)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_types: dict[str, type[Training]] = {'SWM': Swimming,
                                                'RUN': Running,
                                                'WLK': SportsWalking}
    if workout_type in workout_types:
        return workout_types[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
