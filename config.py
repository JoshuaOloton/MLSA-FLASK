class Config:
    DEBUG=True


class TestConfig:
    TESTING = True

    
config = {
    'development': Config,
    'testing': TestConfig
}