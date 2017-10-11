def createVocabList(dataSet):
    """
    ��ȡ���е��ʵļ���
    :param dataSet: ���ݼ�
    :return: ���е��ʵļ���(�������ظ�Ԫ�صĵ����б�)
    """
    vocabSet = set([])  # create empty set
    for document in dataSet:
        # ������ | �������������ϵĲ���
        vocabSet = vocabSet | set(document)  # union of the two sets
    return list(vocabSet)
