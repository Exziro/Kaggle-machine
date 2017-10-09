def chooseBestFeatureToSplit(dataSet):
    """chooseBestFeatureToSplit(ѡ����õ�����)

    Args:
        dataSet ���ݼ�
    Returns:
        bestFeature ���ŵ�������
    """
    # ���һ���ж����е� Feature, ���һ����label����
    numFeatures = len(dataSet[0]) - 1
    # ���ݼ���ԭʼ��Ϣ��
    baseEntropy = calcShannonEnt(dataSet)
    # ���ŵ���Ϣ����ֵ, �����ŵ�Featurn���
    bestInfoGain, bestFeature = 0.0, -1
    # iterate over all the features
    for i in range(numFeatures):
        # create a list of all the examples of this feature
        # ��ȡ��Ӧ��feature�µ���������
        featList = [example[i] for example in dataSet]
        # get a set of unique values
        # ��ȡ���غ�ļ��ϣ�ʹ��set��list���ݽ���ȥ��
        uniqueVals = set(featList)
        # ����һ����ʱ����Ϣ��
        newEntropy = 0.0
        # ����ĳһ�е�value���ϣ�������е���Ϣ�� 
        # ������ǰ�����е�����Ψһ����ֵ����ÿ��Ψһ����ֵ����һ�����ݼ����������ݼ�������ֵ����������Ψһ����ֵ�õ�������͡�
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            # �������
            prob = len(subDataSet)/float(len(dataSet))
            # ������Ϣ��
            newEntropy += prob * calcShannonEnt(subDataSet)
        # gain[��Ϣ����]: �������ݼ�ǰ�����Ϣ�仯�� ��ȡ��Ϣ������ֵ
        # ��Ϣ�������صļ��ٻ�������������ȵļ��١���󣬱Ƚ����������е���Ϣ���棬��������������ֵ�����ֵ��
        infoGain = baseEntropy - newEntropy
        print 'infoGain=', infoGain, 'bestFeature=', i, baseEntropy, newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature