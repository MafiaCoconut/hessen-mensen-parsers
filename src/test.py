# # # from pydantic_settings import BaseSettings, SettingsConfigDict
# # # from pydantic import Field
# # #
# # # class DBSettings(BaseSettings):
# # #     MODE: str
# # #     # DB_HOST: str = Field(..., env='DB_HOST')
# # #     # DB_PORT: int = Field(..., env='DB_PORT')
# # #     # DB_USER: str = Field(..., env='DB_USER')
# # #     # DB_PASSWORD: str = Field(..., env='DB_PASSWORD')
# # #     # DB_NAME: str = Field(..., env='DB_NAME')
# # #     DB_HOST: str
# # #     DB_PORT: int
# # #     DB_USER: str
# # #     DB_PASSWORD: str
# # #     DB_NAME: str
# # #
# # #     @property
# # #     def DATABASE_URL_asyncpg(self):
# # #         return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
# # #
# # #     @property
# # #     def DATABASE_URL_psycopg(self):
# # #         return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
# # #
# # #     model_config = SettingsConfigDict(env_file="../.env", extra="ignore")
# # #
# # # db_settings = DBSettings()
# # #
# # # from sqlalchemy.ext.declarative import declarative_base
# # # from sqlalchemy import create_engine
# # #
# # # from sqlalchemy.orm import sessionmaker
# # # from sqlalchemy.orm import sessionmaker, DeclarativeBase
# # #
# # # class Base(DeclarativeBase):
# # #     pass
# # #
# # # sync_engine = create_engine(
# # #     db_settings.DATABASE_URL_psycopg,
# # #     echo=True,
# # #     pool_size=10,
# # #     max_overflow=20,
# # #     pool_timeout=30,
# # #     pool_recycle=1800,
# # #     pool_pre_ping=True,
# # # )
# # #
# # # session_factory = sessionmaker(bind=sync_engine)
# #
# # from base import Base, sync_engine
# # from canteens import CanteensOrm
# #
# # # from sqlalchemy.orm import Mapped, mapped_column
# # # from sqlalchemy import Integer, String, inspect
# # #
# # # class CanteensOrm(Base):
# # #     __tablename__ = 'canteens'
# # #     __table_args__ = {'extend_existing': True}
# # #
# # #     canteen_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
# # #     name: Mapped[str] = mapped_column(String, nullable=False)
# # #     description: Mapped[str] = mapped_column(String, nullable=True)
# # #     opened_time: Mapped[int] = mapped_column(Integer, nullable=False)
# # #     closed_time: Mapped[int] = mapped_column(Integer, nullable=False)
# # #     created_at: Mapped[int] = mapped_column(Integer, nullable=False)
# #
# #
# # def initialize_database():
# #     print("Создание таблиц в базе данных...")
# #     # Base.metadata.create_all(sync_engine)
# #     print(Base.metadata.tables)
# #
# #     # print(Base)
# #     print(Base.metadata.info)
# #     print("Таблицы созданы.")
# #
# #     from sqlalchemy import inspect
# #     inspector = inspect(sync_engine)
# #     tables = inspector.get_table_names()
# #     print(f"Существующие таблицы: {tables}")
# #
# #
# # if __name__ == "__main__":
# #     initialize_database()
# #     print('База данных инициализирована')
# #
#
#
# import torchaudio
# import torchaudio.transforms as transforms
# import soundfile as sf
# import librosa
#
# # Load the audio file
# audio_path = 'audio_2024-06-26_15-58-42.ogg'
# y, sr = librosa.load(audio_path, sr=16000)
#
# # Save the audio file in wav format for the ASR model
# wav_path = 'audio_2024-06-26_15-58-42.wav'
# sf.write(wav_path, y, sr)
#
# # Load the wav file
# waveform, sample_rate = torchaudio.load(wav_path)
#
# # Load the pre-trained model
# bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
# model = bundle.get_model()
#
# # Transform the audio to match the input format of the model
# transform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
# waveform = transform(waveform)
#
# # Ensure the waveform is mono
# if waveform.shape[0] > 1:
#     waveform = torch.mean(waveform, dim=0, keepdim=True)
#
# # Pass the waveform through the model to get predictions
# with torch.inference_mode():
#     emissions, _ = model(waveform)
#
# # Decode the emissions to text
# decoder = bundle.get_decoder()
# transcript = decoder(emissions[0])
#
# print("Распознанный текст:", transcript)
