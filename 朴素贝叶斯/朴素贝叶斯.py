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
def setOfWords2Vec(vocabList, inputSet):
    """
    �����鿴�õ����Ƿ���֣����ָõ����򽫸õ�����1
    :param vocabList: ���е��ʼ����б�
    :param inputSet: �������ݼ�
    :return: ƥ���б�[0,1,0,1...]������ 1��0 ��ʾ�ʻ���еĵ����Ƿ��������������ݼ���
    """
    # ����һ���ʹʻ��ȳ���������������Ԫ�ض�����Ϊ0
    returnVec = [0] * len(vocabList)# [0,0......]
    # �����ĵ��е����е��ʣ���������˴ʻ���еĵ��ʣ���������ĵ������еĶ�Ӧֵ��Ϊ1
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec
	def _trainNB0(trainMatrix, trainCategory):
    """
    ѵ������ԭ��
    :param trainMatrix: �ļ����ʾ��� [[1,0,1,1,1....],[],[]...]
    :param trainCategory: �ļ���Ӧ�����[0,1,1,0....]���б��ȵ��ڵ��ʾ����������е�1�����Ӧ���ļ����������ļ���0�����������Ծ���
    :return:
    """
    # �ļ���
    numTrainDocs = len(trainMatrix)
    # ������
    numWords = len(trainMatrix[0])
    # �������ļ��ĳ��ָ��ʣ���trainCategory�����е�1�ĸ�����
    # ����ľ��Ƕ��ٸ��������ļ������ļ�����������͵õ����������ļ��ĳ��ָ���
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # ���쵥�ʳ��ִ����б�
    p0Num = zeros(numWords) # [0,0,0,.....]
    p1Num = zeros(numWords) # [0,0,0,.....]

    # �������ݼ����ʳ�������
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocs):
        # �Ƿ����������ļ�
        if trainCategory[i] == 1:
            # ������������ļ������������ļ����������мӺ�
            p1Num += trainMatrix[i] #[0,1,1,....] + [0,1,1,....]->[0,2,2,...]
            # �������е�����Ԫ�ؽ�����ͣ�Ҳ���Ǽ��������������ļ��г��ֵĵ�������
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # ���1�����������ĵ���[P(F1|C1),P(F2|C1),P(F3|C1),P(F4|C1),P(F5|C1)....]�б�
    # �� ��1����£�ÿ�����ʳ��ֵĸ���
    p1Vect = p1Num / p1Denom# [1,2,3,5]/90->[1/90,...]
    # ���0���������ĵ���[P(F1|C0),P(F2|C0),P(F3|C0),P(F4|C0),P(F5|C0)....]�б�
    # �� ��0����£�ÿ�����ʳ��ֵĸ���
    p0Vect = p0Num / p0Denom
    return p0Vect, p1Vect, pAbusive
	
	
	def trainNB0(trainMatrix, trainCategory):
    """
    ѵ�������Ż��汾
    :param trainMatrix: �ļ����ʾ���
    :param trainCategory: �ļ���Ӧ�����
    :return:
    """
    # ���ļ���
    numTrainDocs = len(trainMatrix)
    # �ܵ�����
    numWords = len(trainMatrix[0])
    # �������ļ��ĳ��ָ���
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # ���쵥�ʳ��ִ����б�
    # p0Num ������ͳ��
    # p1Num �����ͳ��
    p0Num = ones(numWords)#[0,0......]->[1,1,1,1,1.....]
    p1Num = ones(numWords)

    # �������ݼ����ʳ���������2.0��������/ʵ�ʵ�����������ĸ��ֵ��2��Ҫ�Ǳ����ĸΪ0����Ȼֵ���Ե�����
    # p0Denom ������ͳ��
    # p1Denom �����ͳ��
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            # �ۼ�����ʵ�Ƶ��
            p1Num += trainMatrix[i]
            # ��ÿƪ���µ������Ƶ�� ����ͳ�ƻ���
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # ���1�����������ĵ���[log(P(F1|C1)),log(P(F2|C1)),log(P(F3|C1)),log(P(F4|C1)),log(P(F5|C1))....]�б�
    p1Vect = log(p1Num / p1Denom)
    # ���0���������ĵ���[log(P(F1|C0)),log(P(F2|C0)),log(P(F3|C0)),log(P(F4|C0)),log(P(F5|C0))....]�б�
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive